from .helpers import *
from .utility_functions.createGridUtility import grid_utility
from itertools import combinations

class POMDP:
    def __init__(self, 
            gridSize : tuple[int, int], 
            nodes : set[Node] = set(), 
            edges : set[Edge] = set(), 
            target : Node = None, 
            model : str = None,
            budget : int = None,
        ) -> None:
        self.gridSize = gridSize
        self.target = target
        
        self.nodes = nodes
        self.edges = edges
        self.strat_edges : set[Edge] = set()
        
        self.model = model
        self.budget = budget
        
        # self.strategies : set[Strategy] = set()
        
        if nodes and edges: self.graph = Graph(nodes, edges)
        else: self.generate_model()
    
    @property
    def ordered_nodes(self) -> list[Node]:
        return sorted(self.nodes)
    
    @property
    def list_nodes(self) -> list[Node]:
        """
        Converts the set of nodes into a list of nodes for indexing purposes.

        Returns:
            list[Node]: the list of nodes
        """
        return list(self.nodes)
    
    def generate_model(self):
        if self.model == 'grid':
            size = self.gridSize[0]
            for i in range(size):
                for j in range(size):
                    self.nodes.add(Node(i, j))
            for i in range(size):
                for j in range(size):
                    if i < size - 1: self.edges.add(Edge((Node(i, j), Node(i+1, j))))
                    if j < size - 1: self.edges.add(Edge((Node(i, j), Node(i,j+ 1))))
        self.graph = Graph(self.nodes, self.edges)
        
    def add_strat_edge(self, edge : Edge):
        self.strat_edges.add(edge)
    
    def step(self, pos, action):
        if action == Action.UP:
            if pos.i > 0: return Node(pos.i - 1, pos.j)
            else: return Node(pos.i, pos.j)
        elif action == Action.RIGHT:
            if pos.j < self.gridSize[1] - 1: return Node(pos.i, pos.j + 1)
            else: return Node(pos.i, pos.j)
        elif action == Action.DOWN:
            if pos.i < self.gridSize[0] - 1: return Node(pos.i + 1, pos.j)
            else: return Node(pos.i, pos.j)
        elif action == Action.LEFT:
            if pos.j > 0: return Node(pos.i, pos.j - 1)
            else: return Node(pos.i, pos.j)
    
    def observe_actions(self, n : Node) -> set[Action]:
        adjacent_edges = self.graph.get_edges(n)
        actions = set()
        for e in adjacent_edges:
            if e.i == n.i:
                if e.j > n.j: actions.add(Action.RIGHT)
                else: actions.add(Action.LEFT)
            else:
                if e.i > n.i: actions.add(Action.DOWN)
                else: actions.add(Action.UP) 
        return actions
    
    def distance(self, n1 : Node, n2 : Node) -> int:
        return abs(n1.i - n2.i) + abs(n1.j - n2.j)
    
    def reward(self, pos, action : Action):
        """
        The reward of an action is the expected value of the action.
        The distance to the target is the negative reward.

        Args:
            action (Action): _description_
        """
        
        # even if the action connects with a pre existing node in the strategy
        # the reward is the same since the target might be closer through a
        # different path

        pomdp_copy = deepcopy(self)
        next_node = pomdp_copy.step(pos, action)
        # if next_node is None: return -float('inf')
        return -self.distance(next_node, self.target)

    def translate_grid_coords_to_grid_id(self, pos : Node) -> int:
        return pos.i * self.gridSize[0] + pos.j
    
    def translate_grid_id_to_grid_coords(self, id : int) -> Node:
        return Node(id // self.gridSize[0], id % self.gridSize[0])
    
    def utility(self, strategies : dict[int, Strategy], assignments : dict[Node, int]) -> float:
        if (self.model == 'grid'):
            # translate layer
            # modify the node coordinates into grid ids for the OOP library
            target = self.translate_grid_coords_to_grid_id(pos = self.target)
            
            for n in self.nodes: n.id = self.translate_grid_coords_to_grid_id(n)
            u, parsed_pomdp = grid_utility(self.budget, target, self.gridSize[0], strategies, assignments)
            return u, parsed_pomdp
        else:
            raise NotImplementedError("Utility function not implemented for this model")
    
    def solve(self) -> set[Edge]:
        infinite_budget_optimal_solution, minimal_budget_optimal_solution = None, None
        
        if self.budget is None: self.budget = len(self.nodes)

        # [Finding the optimal solution with infinite budget]
        used_actions : set[Action]  = set()
        for n in self.nodes:
            agent = Agent(n)
            while agent.pos != self.target:
                action, suitable_actions = agent.choose_action(self)
                used_actions.add(action)
                # agent.pos.strategy = Strategy({ action : 1.0 })
                agent.pos.set_suitable_actions(suitable_actions) # add the possible actions to the node
                prev_agent_pos = agent.pos
                agent.pos = self.step(agent.pos, action) # advance the agent
                new_edge = Edge((prev_agent_pos, agent.pos))
                
                # [OPTIMIZATION]
                # if the edge is already in the strategy, then we have already found a path from the 
                # current agent node to the target node
                if new_edge in self.strat_edges: break 
                
                self.add_strat_edge(new_edge)
                
        # We check if the optimal solution is below the required budget
        # otherwise we recompute the solution with non-determinism in mind
        # where each strategy is a probability distribution between the actions
        if len(used_actions) > self.budget:
            print("[Found optimal solution with infinite budget, adjusting for given budget...]")
            
            # # iterate through all the nodes to find the possible strategies
            # possible_strategies : set[set[Strategy]] = set(set())
            # for n in self.nodes:
            #     if n == self.target: continue
                
            #     # for each node, add all action combinations as new strategies
            #     # print(n, n.suitable_actions)
            #     for i in range(len(n.suitable_actions)):    
            #         for comb in set(combinations(n.suitable_actions, i+1)):
            #             # print({action: RangeFloat(1 / (i+1)) for action in comb})
            #             possible_strategies.add(Strategy(actions = {action: RangeFloat(1 / (i+1)) for action in comb}))

            # # the possible strategies within the given budget (budget or less) are all 
            # # the combinations of size 1 to B of the possible strategies
            # available_strategy_combinations = set()
            # for i in range(1, self.budget+1):
            #     available_strategy_combinations.update(set(combinations(possible_strategies, i)))

            
            # for n in self.ordered_nodes:
            #     if n == self.target: continue
                
            #     # we know that possible strategies are by definition less suitable than the suitable strategies,
            #     # however we need to include them if we want to find the optimal strategy within a given budget
            #     # as one node's unoptimal strategy could still lead to the optimal low budget solution
                
            #     # # [Finding suitable strategies]
            #     # for strategy in possible_strategies:
            #     #     # the strategies that are a subset of the node's possible actions
            #     #     # i.e. if the node can perform all the actions in the strategy
                    
            #     #     print(n, n.suitable_actions, strategy.actions.keys(), n.suitable_actions.issubset(set(strategy.actions.keys())))
            #     #     if n.suitable_actions.issubset(set(strategy.actions.keys())):
            #     #     # if set(strategy.actions.keys()).issubset(n.suitable_actions):
            #     #         n.suitable_strategies.add(strategy)
                
            #     # # shorthand for the above commented code
            #     # n.suitable_strategies = n.suitable_strategies.union(set(strategy for strategy in possible_strategies if n.suitable_actions.issubset(set(strategy.actions.keys()))))
                
            #     # [Finding possible strategies]
            #     for strategy in possible_strategies:
            #         # add all strategies that contain at least one action 
            #         # that the node can perform; possible strategies
            #         if any([action in n.suitable_actions for action in strategy.actions.keys()]):
            #             n.possible_strategies.add(strategy)                
            
            
            # for i in range(len(n.suitable_actions)):    
            #     for comb in set(combinations(n.suitable_actions, i+1)):
            #         # print({action: RangeFloat(1 / (i+1)) for action in comb})
            #         possible_strategies.add(Strategy(actions = {action: RangeFloat(1 / (i+1)) for action in comb}))
            
            strategies : set[Action] = set()
            for i in range(len(used_actions)):
                for comb in set(combinations(used_actions, i+1)):
                    strategies.add(Strategy(actions = {action: RangeFloat(1 / (i+1)) for action in comb}))
                
            strategy_combinations = set()
            for i in range(self.budget):
                strategy_combinations |= set(combinations(strategies, i+1))
            
            def get_best_strategy_assignment(strategy_combination : set[Strategy], nodes : list[Node]):
                # 1-indexed startegy id numbering
                # id_strategy_combination = dict(map(lambda kv : (kv[0] + 1, kv[1]), id_strategy_combination.items()))
                id_strategy_combination = dict(enumerate(strategy_combination, start=1))
                
                def try_all_from_node(i : int):
                    """
                    Args:
                        i (int): the index of the list of nodes to try from 
                        (not to be confused with the node id or its coordinates)
                    """
                    
                    if i >= len(nodes):
                        assignments = {n: n.strategy_id for n in nodes if n != self.target}
                        u, parsed_pomdp = self.utility(id_strategy_combination, assignments)
                        print(id_strategy_combination)
                        print(u, parsed_pomdp)
                        return [{
                            'utility': u,
                            'assignments': assignments,
                            'strategy_combination': id_strategy_combination,
                            'parsed_pomdp': parsed_pomdp,
                        }]

                    node = nodes[i]
                    if node == self.target: return try_all_from_node(i + 1)

                    results = list()
                    for id, strat in id_strategy_combination.items():
                        # if strat in node.possible_strategies:
                        node.assign_strategy(strat, id)
                        result = try_all_from_node(i + 1)
                        if result: results.extend(result)
                    
                    return results

                return try_all_from_node(0)
            
            
            # [Finding the optimal solution within the given budget using non-determinism]
            # Algorithm relies on recursion to try all possible combinations of strategies
            # Order of the nodes is not imperative since all combinations are tried regardless of order
            # and one node's strategy cannot affect another node's strategy in this implementation.
            best_strategy_assignments = list()
            
            # we precompute the list of nodes since it takes O(n) time to convert the set to a list
            # and it is favourable to compute it once before the recursive function is called.
            # this way we reduce the time complexity to O(n) instead of O(n^2)
            nodes = self.list_nodes
            # for strategy_combination in available_strategy_combinations:
            for strategy_combination in strategy_combinations:
                best_strategy = get_best_strategy_assignment(strategy_combination, nodes)
                if best_strategy: best_strategy_assignments.extend(best_strategy)
            # print(best_strategy_assignments)
            minimal_budget_optimal_solution = max(best_strategy_assignments, key = lambda x: x['utility'])
        else:
            strategies = set(Strategy({ action : 1.0 } for action in used_actions))
            id_strategy_combination = dict(enumerate(strategies, start=1))
            # assignments = {n: n.strategy_id for n in self.nodes if n != self.target}
            for n in self.nodes:
                if n == self.target: continue
                for s_id, s in id_strategy_combination.items():
                    if s == n.strategy: n.strategy_id = s_id
            
            _, infinite_budget_optimal_solution = self.utility(id_strategy_combination, {n: n.strategy_id for n in self.nodes if n != self.target})
            
        return infinite_budget_optimal_solution, minimal_budget_optimal_solution

        
class Agent:
    def __init__(self, pos : Node) -> None:
        self.pos = pos # intial state
    
    def choose_action(self, pomdp : POMDP) -> Action:
        available_actions = pomdp.observe_actions(self.pos)
        expectedMoveValue = {a : pomdp.reward(self.pos, a) for a in available_actions}
        # for a in available_actions: expectedMoveValue[a] = pomdp.reward(self.pos, a)
        max_value = max(expectedMoveValue.values()) # maximum expected value
        max_keys = set(key for key, value in expectedMoveValue.items() if value == max_value) # all actions with the maximum expected value
        return max(expectedMoveValue, key = lambda k: expectedMoveValue[k]), max_keys
        


if __name__ == '__main__':
    
    # rf = RangeFloat(0.5)  # Initialize with a value
    # print(rf.value)  # Output: 0.5

    # rf.value = 0.7  # Set a new value
    # print(rf.value)  # Output: 0.7

    # rf.value = 1.5  # Trying to set an invalid value
    # # Output: ValueError: Value must be between 0 and 1

    
    # pomdp = POMDP(gridSize=(2, 2), target=Node(1, 1), model='grid', budget=1)
    pomdp = POMDP(gridSize=(3, 3), target=Node(2,1), model='grid', budget=2)
    infinite_budget_optimal_solution, minimal_budget_optimal_solution = pomdp.solve()
    print(minimal_budget_optimal_solution)


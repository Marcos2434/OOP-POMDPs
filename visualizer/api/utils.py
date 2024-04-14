from enum import Enum
from copy import deepcopy

import numpy as np
from itertools import combinations

class Action(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    
    def __str__(self):
        # capitalize the first letter of the action while the rest is lowercase
        return self.name[0] + self.name[1:].lower()
    
    def __repr__(self):
        return self.name[0]

    def __eq__(self, value: object) -> bool:
        return super().__eq__(value)
    
    def __hash__(self) -> int:
        return hash(self.name)
    

class RangeFloat:
    def __init__(self, value=0.0):
        self._value = value
        self.value = value  # utilize setter to ensure value is within range
    
    @property
    def value(self) -> float:
        # when one accesses the value attribute, this function is called
        return self._value
    
    @value.setter
    def value(self, new_value) -> None:
        # when one sets the value attribute, this function is called
        if 0.0 <= float(new_value) <= 1.0: self._value = float(new_value)
        else: raise ValueError("Value must be between 0 and 1")
    
    def __eq__(self, other) -> bool:
        return isinstance(other, RangeFloat) and self._value == other._value
    
    def __hash__(self) -> int:
        return hash(self._value)
    
    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return str(self._value)

class Strategy:
    def __init__(self, actions : dict[Action, RangeFloat] = None) -> None:
        self.actions : dict[Action, RangeFloat] = actions
    
    def add_action(self, action : Action, p : RangeFloat):
        self.actions[action] = p
        
    def __str__(self) -> str:
        return str(self.actions)
    
    def __repr__(self) -> str:
        return str(self.actions)
    
    def __hash__(self) -> int:
        return hash(tuple(self.actions.items()))

    def __eq__(self, other) -> bool:
        return isinstance(other, Strategy) and self.actions == other.actions

class Node:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j
        self.suitable_actions : set[Action] = set()
        self.suitable_strategies : set[Strategy] = set()
        self.possible_strategies : set[Strategy] = set()
        
    def __hash__(self):
        return hash((self.i, self.j))
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Node) and self.i == other.i and self.j == other.j
    
    def __str__(self) -> str:
        return f'({self.i}, {self.j})'
    
    def __repr__(self) -> str:
        return f'({self.i}, {self.j})'
    
    def assign_strategy(self, strategy : Strategy):
        self.strategy = strategy
    
    def set_suitable_actions(self, suitable_actions : set[Action]):
        self.suitable_actions = suitable_actions
        
    def __gt__(self, other):
        return self.i > other.i or (self.i == other.i and self.j > other.j)
    
class Edge:
    def __init__(self, nodes : tuple[Node, Node]) -> None:
        self.nodes = nodes
    
    def __hash__(self):
        return hash(self.nodes)
    
    def __str__(self) -> str:
        return f'{self.nodes[0]} -> {self.nodes[1]}'

    def __repr__(self) -> str:
        return f'{self.nodes[0]} -> {self.nodes[1]}'
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Edge) and self.nodes == other.nodes


class Graph:
    def __init__(self, nodes : set[Node], edges : set[Edge]) -> None:
        self.nodes = nodes
        self.edges = edges
        
        self.adjacency_list = {}
        for edge in edges:
            if edge.nodes[0] not in self.adjacency_list: self.adjacency_list[edge.nodes[0]] = []
            if edge.nodes[1] not in self.adjacency_list: self.adjacency_list[edge.nodes[1]] = []
            
            self.adjacency_list[edge.nodes[0]].append(edge.nodes[1])
            self.adjacency_list[edge.nodes[1]].append(edge.nodes[0])
    
    def __str__(self) -> str:
        return str(self.adjacency_list)
    
    def get_edges(self, n : Node) -> set[Node]:
        return self.adjacency_list.get(n, [])

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

    def utility(self) -> float:
        return 1.0
        # return sum([self.reward(edge.nodes[0], edge.nodes[1]) for edge in self.strat_edges])
    
    def solve(self) -> set[Edge]:
        if self.budget is None: self.budget = len(self.nodes)

        # [Finding the optimal solution with infinite budget]
        strategies = set()
        for n in self.nodes:
            agent = Agent(n)
            while agent.pos != self.target:
                action, suitable_actions = agent.choose_action(self)
                strategies.add(action) # no need to use the strategy class since actions are deterministic
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
        if len(strategies) > self.budget:
            print("[Found optimal solution with infinite budget, adjusting for given budget...]")
            
            # iterate through all the nodes to find the possible strategies
            possible_strategies : set[set[Strategy]] = set(set())
            for n in self.nodes:
                if n == self.target: continue
                
                # for each node, add all action combinations as new strategies
                for i in range(len(n.suitable_actions)):
                    for comb in set(combinations(n.suitable_actions, i+1)):
                        possible_strategies.add(Strategy(actions = {action: RangeFloat(1 / (i+1)) for action in comb}))

            # the possible strategies within the given budget (budget or less) are all 
            # the combinations of size 1 to B of the possible strategies
            available_strategy_combinations = set()
            for i in range(1, self.budget+1):
                available_strategy_combinations.update(set(combinations(possible_strategies, i)))

            
            for n in self.ordered_nodes:
                if n == self.target: continue
                
                # we know that possible strategies are by definition less suitable than the suitable strategies,
                # however we need to include them if we want to find the optimal strategy within a given budget
                # as one node's unoptimal strategy could still lead to the optimal low budget solution
                
                # [Finding suitable strategies]
                # for strategy in possible_strategies:
                #     # the strategies that are a subset of the node's possible actions
                #     # i.e. if the node can perform all the actions in the strategy
                    
                #     print(n, n.suitable_actions, strategy.actions.keys(), n.suitable_actions.issubset(set(strategy.actions.keys())))
                #     if n.suitable_actions.issubset(set(strategy.actions.keys())):
                #     # if set(strategy.actions.keys()).issubset(n.suitable_actions):
                #         n.suitable_strategies.add(strategy)
                
                # shorthand for the above commented code
                # n.suitable_strategies = n.suitable_strategies.union(set(strategy for strategy in possible_strategies if n.suitable_actions.issubset(set(strategy.actions.keys()))))
                
                # [Finding possible strategies]
                for strategy in possible_strategies:
                    # add all strategies that contain at least one action 
                    # that the node can perform; possible strategies
                    
                    if any([action in n.suitable_actions for action in strategy.actions.keys()]):
                        n.possible_strategies.add(strategy)                

            def get_best_strategy_assignment(strategy_combination : set[Strategy]):
                def try_all_from_node(i : int):
                    if i >= len(self.nodes):
                        return [{
                            'utility': self.utility(),
                            'assignments': {node: node.strategy for node in self.nodes if node != self.target}
                        }]

                    node = self.ordered_nodes[i]
                    if node == self.target: return try_all_from_node(i + 1)

                    results = list()
                    for strat in strategy_combination:
                        if strat in node.possible_strategies:
                            node.assign_strategy(strat)
                            result = try_all_from_node(i + 1)
                            if result: results.extend(result)
                    
                    return results

                return try_all_from_node(0)
            
            
            # [Finding the optimal solution within the given budget using non-determinism]
            # Algorithm relies on recursion to try all possible combinations of strategies
            # Order of the nodes is not imperative since all combinations are tried regardless of order
            # and one node's strategy cannot affect another node's strategy in this implementation.
            best_strategy_assignments = list()
            for strategy_combination in available_strategy_combinations:
                bs = get_best_strategy_assignment(strategy_combination)
                if bs: best_strategy_assignments.extend(bs)
            best_strategy_assignment = max(best_strategy_assignments, key = lambda x: x['utility'])

        return self.strat_edges, best_strategy_assignment

        
class Agent:
    def __init__(self, pos : Node) -> None:
        self.pos = pos # intial state
    
    def choose_action(self, pomdp : POMDP) -> Action:
        available_actions = pomdp.observe_actions(self.pos)
        expectedMoveValue = {}
        for a in available_actions:
            expectedMoveValue[a] = pomdp.reward(self.pos, a)
        max_value = max(expectedMoveValue.values())
        max_keys = set(key for key, value in expectedMoveValue.items() if value == max_value)
        return max(expectedMoveValue, key = lambda k: expectedMoveValue[k]), max_keys
        


if __name__ == '__main__':
    
    # rf = RangeFloat(0.5)  # Initialize with a value
    # print(rf.value)  # Output: 0.5

    # rf.value = 0.7  # Set a new value
    # print(rf.value)  # Output: 0.7

    # rf.value = 1.5  # Trying to set an invalid value
    # # Output: ValueError: Value must be between 0 and 1

    
    pomdp = POMDP(gridSize=(2, 2), target=Node(1, 1), model='grid', budget=1)
    # pomdp = POMDP(gridSize=(3, 3), target=Node(2,1), model='grid', budget=2)
    infinite_budget_optimal_solution_edges, minimal_budget_optimal_solution = pomdp.solve()


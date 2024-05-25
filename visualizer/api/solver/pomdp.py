from itertools import combinations, product
import plotly.graph_objects as go
import os
import random

FILE_PATH_FLAG = True

if FILE_PATH_FLAG:
    # Run directly
    from helpers import *
    from utility_functions.createGridUtility import grid_utility
    DIR_PATH = '/Users/marcos/Documents/github_projects/POMDPs/visualizer/api/solver/utility_functions/generated_models/'
else:
    # Run through server (Django)
    from .helpers import *
    from .utility_functions.createGridUtility import grid_utility
    DIR_PATH = os.getcwd() + '/api/solver/utility_functions/generated_models/'

from numpy.typing import *
import numpy as np

class POMDP:
    def __init__(self, 
            gridSize : tuple[int, int], 
            nodes : set[Node] = set(), 
            edges : set[Edge] = set(), 
            target : Node = None, 
            model : str = None,
            budget : int = None,
        ) -> None:
        self.gridSize : tuple[int, int] = gridSize
        self.target : Node = target
        
        self.nodes : set[Node] = nodes
        self.edges : set[Edge] = edges
        self.strat_edges : set[Edge] = set()
        
        self.model : str = model
        self.budget : int = budget
        
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
            for i in range(self.gridSize[0]):
                for j in range(self.gridSize[1]):
                    self.nodes.add(Node(i, j))
            for i in range(self.gridSize[0]):
                for j in range(self.gridSize[1]):
                    if i < self.gridSize[0] - 1: self.edges.add(Edge((Node(i, j), Node(i+1, j))))
                    if j < self.gridSize[1] - 1: self.edges.add(Edge((Node(i, j), Node(i,j+ 1))))
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
    
    def heuristic_reward(self, pos, action : Action):
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
    
    def utility(self, strategies : dict[int, Strategy], observations : dict[Node, int]) -> float:
        if (self.model == 'grid'):
            # translate layer
            # modify the node coordinates into grid ids for the OOP library
            target = self.translate_grid_coords_to_grid_id(pos = self.target)
            
            for n in self.nodes: n.id = self.translate_grid_coords_to_grid_id(n)
            exp_min_rew, parsed_pomdp = grid_utility(self.budget, target, self.gridSize[0], strategies, observations)
            u = 1/exp_min_rew if exp_min_rew != 0 else 0
            return u, parsed_pomdp
        else:
            raise NotImplementedError("Utility function not implemented for this model")
    
    def generate_points(self, strategies : dict[int, Strategy], observations : dict[Node, int], sections = 5, write_to_file = False) -> set[ArrayLike]:
        # generate all possible combinations of action probabilities depending on
        # how many sections we want to divide the probability space into
        probabilities = [frac(i, (sections - 1)) for i in range(sections)]
        
        strategy_points = []
        for _, s in strategies.items():
            actions = s.actions.keys()
            
            # get all proper uniformly distributed combinations of action probabilities
            combinations_ = np.array([ comb for comb in product(probabilities, repeat=len(actions)) if sum(comb) == 1 ])
            points = np.full((len(combinations_), len(Action)), frac(0))
            for j in range(points.shape[0]):
                for k, a in enumerate(actions):
                    points[j][a.value] = combinations_[j][k]
            strategy_points.append(points)
        
        # combinations of all properly distributed probabilities of each strategy
        combinations_ = np.array(list(product(*strategy_points)))        
        
        U = np.empty(len(combinations_))
        for i in range(len(U)):
            # update each strategy with the action probabilities
            for j in range(len(strategies)):
                strategies[j+1].actions = {a: combinations_[i][j][a.value] for a in Action}

            # compute the utility of the strategies
            U[i], _ = self.utility(strategies, observations)
            
            # U[i] = inverse_fraction(u) # take the inverse of the utility as a fraction
            # U[i] = 1/u if u != 0 else 0 # take the inverse of the utility
        
        # standardize U
        # U = (U - U.min()) / (U.max() - U.min())
        
        if write_to_file:
            with open(DIR_PATH + 'points.txt', 'w') as f:
                for i in range(len(combinations_)):
                    f.write(f'{combinations_[i]} {U[i]}\n')
        
        return combinations_, U
    
    def generate_initial_solution(self, strategies):
        strategy_points = []
        for _, s in strategies.items():
            actions = list(s.actions.keys())
            distribution = list(map(lambda x : frac(x).limit_denominator(), np.random.dirichlet(np.ones(len(actions)))))
            point = [frac(0)] * len(Action)
            for a in Action:
                if a in actions:
                    point[a.value] = distribution.pop()
            strategy_points.append(point)
        return strategy_points
        
        
        # return [[frac(0), frac(1, 2), frac(1, 2), frac(0)]]
    
    def neighbor(self, strategies, solution, neighborhood_scale):
        new_solution = solution.copy()
        for strategy_idx in range(len(solution)):
            actions = strategies[strategy_idx+1].actions.keys()
            
            # [OLD] Perturb the probabilities of actions in each strategy according to a normal distribution centered at 0
            # perturbation = np.random.normal(0, scale=neighborhood_scale, size=len(actions))
            # Normalize the perturbation to ensure the probabilities sum up to 0
            # perturbation -= np.mean(perturbation)
            
            # Perturb the probabilities of actions in each strategy according to a zero-sum distribution
            # print(len(actions)) # for some reason this doesn't work once helpers.py is updated, rerun jupyter file
            perturbation = zero_sum_distribution(size=len(actions), neighborhood_scale=neighborhood_scale)
            # print(np.around(list(map(float, perturbation)), 2))  
            new_probabilities = [frac(0)] * len(Action)
            i = 0
            for a in Action:
                if a in actions: 
                    new_probabilities[a.value] = new_solution[strategy_idx][a.value] + perturbation[i]
                    i += 1
            
            new_probabilities = np.clip(new_probabilities, 0, 1) # ensure that the probabilities sum up to 1
            total_prob = frac(sum(new_probabilities))
            # new_solution[strategy_idx] = new_probabilities
            new_solution[strategy_idx] = [frac(frac(p), total_prob) for p in new_probabilities]
            
            
            
            # update each strategy with the action probabilities 
            strategies = self.assign_point_to_strategies(strategies, new_solution)
        return new_solution, strategies

    def acceptance_probability(self, old_utility, new_utility, temperature):
        # Calculate acceptance probability based on temperature and cost difference
        if new_utility > old_utility: return 1 # accept if the new solution is better
        elif temperature == 0: return 0 
        else: return np.exp((new_utility - old_utility) / temperature) # accept with a probability proportional to the temperature and the difference in cost
    
    def assign_point_to_strategies(self, strategies, point):
        for i in range(len(strategies)):
            strategies[i+1].actions = {a: point[i][a.value] for a in Action if a in strategies[i+1].actions.keys()}
        return strategies
    
    def simulated_annealing(self, strategies, observations, initial_temperature=1.0, cooling_rate=0.1, max_iterations=100, neighborhood_scale=0.1):
        current_solution = self.generate_initial_solution(strategies) # a solution refers to a point, the intial solution is a random point
        strategies = self.assign_point_to_strategies(strategies, current_solution) # assign the initial solution to the strategies
        current_utility, _ = self.utility(strategies, observations)  # Compute cost of initial solution
        
        best_solution = current_solution
        best_utility = current_utility
        temperature = initial_temperature

        points = []
        utilities = []

        for _ in range(max_iterations):
            new_solution, strategies = self.neighbor(strategies, current_solution, neighborhood_scale) # Generate a new solution, i.e. perturb the current solution
            new_utility, _ = self.utility(strategies, observations)  # Compute cost of new solution

            # print(new_utility)
            
            points.append(new_solution)
            utilities.append(new_utility)
            
            # print(f"new solution: {np.around(list(map(float, new_solution[0])), 2)}, new utility: {new_utility}, acceptance probability: {self.acceptance_probability(current_utility, new_utility, temperature)}")
            
            if self.acceptance_probability(current_utility, new_utility, temperature) > random.random():
                current_solution = new_solution
                current_utility = new_utility
                if new_utility > best_utility:
                    best_solution = new_solution
                    best_utility = new_utility
            temperature *= cooling_rate

        return best_solution, best_utility, points, utilities
    
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
                agent.pos.strategy = Strategy({ action : frac(1) })
                # agent.pos.set_suitable_actions(suitable_actions) # add the possible actions to the node
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
            
            # used_actions=[Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]
            
            strategies : set[Action] = set()
            for i in range(len(used_actions)):
                for comb in set(combinations(used_actions, i+1)):
                    strategies.add(Strategy(actions = {action: frac(1, (i+1)) for action in comb}))

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
                        # print(id_strategy_combination)
                        # print(u, parsed_pomdp)
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
                        # if strat in node.possible_strategies: # very small optimization, not worth it
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
            strategies = set(Strategy({ action : frac(1) }) for action in used_actions)
            id_strategy_combination = dict(enumerate(strategies, start=1))
            # assignments = {n: n.strategy_id for n in self.nodes if n != self.target}
            for n in self.nodes:
                if n == self.target: continue
                for s_id, s in id_strategy_combination.items():
                    if s == n.strategy: n.strategy_id = s_id
            print(strategies)
            
            _, resulting_pomdp = self.utility(id_strategy_combination, {n: n.strategy_id for n in self.nodes if n != self.target})
            
            # chnage fractions to approximations for visualizer
            infinite_budget_optimal_solution = {}
            for k, v in resulting_pomdp.items():
                infinite_budget_optimal_solution[k] = float(v)
            
        return infinite_budget_optimal_solution, minimal_budget_optimal_solution


class Agent:
    def __init__(self, pos : Node) -> None:
        self.pos = pos # intial state
    
    def choose_action(self, pomdp : POMDP) -> Action:
        available_actions = pomdp.observe_actions(self.pos)
        expectedMoveValue = {a : pomdp.heuristic_reward(self.pos, a) for a in available_actions}
        # for a in available_actions: expectedMoveValue[a] = pomdp.reward(self.pos, a)
        max_value = max(expectedMoveValue.values()) # maximum expected value
        max_keys = set(key for key, value in expectedMoveValue.items() if value == max_value) # all actions with the maximum expected value
        return max(expectedMoveValue, key = lambda k: expectedMoveValue[k]), max_keys
        

def plot_actions_3D(combinations_, u, actions : list[Action]) -> None:
    mask = np.empty((0, len(Action)))
    for a in actions:
        m = np.zeros(len(Action))
        m[a.value] = 1
        mask = np.vstack((mask, m))
    
    print(mask, mask.shape)
    
    # reduce dimension since B=1 then only one strategy is available
    # only works for B=1
    points = np.empty((combinations_.shape[0], len(Action)))
    for i in range(combinations_.shape[0]):
        points[i] = combinations_[i][0]

    # apply mask to the points to reduce dimension
    points = points @ mask.T

    x, y = points[:, 0], points[:, 1]
    z = u
    
    max_index = np.argmax(u)
    fig = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=8,
            color=['blue' if i != max_index else 'red' for i in range(len(x))],
            opacity=0.8,
            line=dict(color='black', width=1)  # Marker edge color
        ),
    )])

    fig.update_layout(
        # template='plotly_dark', # Dark mode
        template='plotly_white',
        scene=dict(
                xaxis=dict(
                    title=str(actions[0]),
                    range=[0, 1]
                ),
                yaxis=dict(
                    title=str(actions[1]),
                    range=[0, 1]
                ),
                zaxis=dict(
                    title='Utility'
                )
            )
    )

    fig.update_layout(title='3D Scatter Plot')

    fig.show()

def plot_actions_4D(combinations_, u, actions : list[Action]) -> None:
    mask = np.empty((0, len(Action)))
    for a in actions:
        m = np.zeros(len(Action))
        m[a.value] = 1
        mask = np.vstack((mask, m))
    
    # reduce dimension since B=1 then only one strategy is available
    # only works for B=1
    points = np.empty((combinations_.shape[0], len(Action)))
    for i in range(combinations_.shape[0]):
        points[i] = combinations_[i][0]
        
    # apply mask to the points to reduce dimension
    points = points @ mask.T
    
    x, y, z = points[:, 0], points[:, 1], points[:, 2]
    # z = u # pretty cool but wrong hahah
    
    # Scale the fourth dimension values to adjust marker sizes
    max_u = max(u)
    min_u = min(u)
    
    
    if max_u == min_u:
        # If all values are the same, set all sizes to 1
        # and avoid division by zero
        scaled_sizes = [10 for _ in u]
        print("All values are the same, setting all sizes to 10")
    else:
        mini, maxi = 1, 20
        scaled_sizes = [(val - min_u) / (max_u - min_u) * (maxi-mini) + mini for val in u]  # Scale sizes to be between 5 and 55
    
    max_index = np.argmax(u)
    fig = go.Figure(data=go.Scatter3d(
        x=x,
        y=y,
        z=z,
        marker=dict(
            size=scaled_sizes,  # Use the scaled fourth dimension for marker size
            color=['blue' if i != max_index else 'red' for i in range(len(x))],
            opacity=0.7
        ),
        mode='markers',
    ))

    # Customize layout
    fig.update_layout(
        # template='plotly_dark', # Dark mode
        template='plotly_white',
        scene=dict(
            xaxis_title=str(actions[0]),
            yaxis_title=str(actions[1]),
            zaxis_title=str(actions[2]),
        ))

    # Show the plot
    fig.show()



if __name__ == '__main__':
    pass


    budget = 1
    gridSize = (25, 25)
    target = Node(24, 1)
    strategies = list([ 
        Strategy({ Action.DOWN: frac(1, 3), Action.RIGHT: frac(1, 3), Action.LEFT: frac(1, 3) }) 
    ])
    enumerated_strategies = dict(enumerate(strategies, start=1))

    pomdp = POMDP(gridSize=gridSize, target=target, model='grid', budget=budget)

    # Assign strategies to the nodes
    for node in pomdp.nodes: node.assign_strategy(enumerated_strategies[1], 1)
    observations =  {n: n.strategy_id for n in pomdp.nodes if n != target}

    # ---------------------------------------------------------
    # get one specific utility value
    # print(pomdp.utility(enumerated_strategies, assignments)[0])
    # ---------------------------------------------------------

    combinations_, U = pomdp.generate_points(enumerated_strategies, observations, sections=25, write_to_file=True)
    plot_actions_4D(combinations_, U, actions = [Action.DOWN, Action.RIGHT, Action.LEFT])

    # get the probability distribution of the actions that maximizes the utility
    max_index = np.argmax(U)
    approx = np.around(list(map(float, combinations_[max_index][0])), 2)

    print('Max utility value: ')
    print(combinations_[max_index][0])
    print(approx)
    print(U[max_index])



    # budget = 1
    # gridSize = (10, 10)
    # target = Node(9, 9)
    # strategies = list([  
    #     Strategy({ Action.DOWN: frac(1, 2), Action.RIGHT: frac(1, 2) }) 
    # ])
    # enumerated_strategies = dict(enumerate(strategies, start=1))

    # pomdp = POMDP(gridSize=gridSize, target=target, model='grid', budget=budget)

    # # Assign strategies to the nodes
    # for node in pomdp.nodes: node.assign_strategy(enumerated_strategies[1], 1)
    # observations =  {n: n.strategy_id for n in pomdp.nodes if n != target}

    # # ---------------------------------------------------------
    # # get one specific utility value
    # # print(pomdp.utility(enumerated_strategies, assignments)[0])
    # # ---------------------------------------------------------
    # # print(len(pomdp.ordered_nodes))
    # # print(len(observations))

    # initial_temperature = 10.0  # High initial temperature to encourage exploration
    # cooling_rate = 0.99  # Low cooling rate to increase exploitation
    # max_iterations = 200  # Sufficient iterations to explore the search space
    # neighborhood_scale = 0.1  # Small perturbations for neighborhood exploration around (0.5, 0.5)


    # best_solution, best_U, points, utilities = pomdp.simulated_annealing(
    #     enumerated_strategies, 
    #     observations, 
    #     initial_temperature, 
    #     cooling_rate, 
    #     max_iterations, 
    #     neighborhood_scale, 
    # )

    # plot_actions_3D(np.array(points), utilities, actions = [Action.DOWN, Action.RIGHT])

    # approximated_solution = np.around(list(map(float, best_solution[0])), 2)

    # print('Best solution: ', approximated_solution)
    # print('Best utility: ', best_U)

    # budget = 1
    # gridSize = (10, 10)
    # target = Node(9, 9)
    # strategies = list([  
    #     Strategy({ Action.DOWN: frac(1, 2), Action.RIGHT: frac(1, 2) }) 
    # ])
    # enumerated_strategies = dict(enumerate(strategies, start=1))

    # pomdp = POMDP(gridSize=gridSize, target=target, model='grid', budget=budget)

    # # Assign strategies to the nodes
    # for node in pomdp.nodes: node.assign_strategy(enumerated_strategies[1], 1)
    # observations =  {n: n.strategy_id for n in pomdp.nodes if n != target}

    # # ---------------------------------------------------------
    # # get one specific utility value
    # # print(pomdp.utility(enumerated_strategies, assignments)[0])
    # # ---------------------------------------------------------
    # # print(len(pomdp.ordered_nodes))
    # # print(len(observations))

    # initial_temperature = 10.0  # High initial temperature to encourage exploration
    # cooling_rate = 0.01  # Gradual cooling rate to balance exploration and exploitation
    # max_iterations = 50  # Sufficient iterations to explore the search space
    # neighborhood_scale = 0.1  # Small perturbations for neighborhood exploration

    # best_solution, best_U = pomdp.simulated_annealing(
    #     enumerated_strategies, 
    #     observations, 
    #     initial_temperature, 
    #     cooling_rate, 
    #     max_iterations, 
    #     neighborhood_scale, 
    # )

    # approximated_solution = np.around(list(map(float, best_solution[0])), 2)

    # print('Best solution: ', approximated_solution)
    # print('Best utility: ', best_U)
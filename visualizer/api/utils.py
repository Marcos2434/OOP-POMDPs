from enum import Enum
from copy import deepcopy

import numpy as np

class Action:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class RangeFloat:
    def __init__(self, value=0.0):
        self._value = value
        self.value = value  # utilize setter to ensure value is within range
    
    @property
    def value(self):
        # when one accesses the value attribute, this function is called
        return self._value 
    
    @value.setter
    def value(self, new_value):
        # when one sets the value attribute, this function is called
        if 0.0 <= new_value <= 1.0: self._value = new_value
        else: raise ValueError("Value must be between 0 and 1")
    

class Strategy:
    def __init__(self) -> None:
        self.actions : dict[Action, RangeFloat] = None
    
    def add_action(self, action : Action, p : RangeFloat):
        self.actions[action] = p

class Node:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j
    
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
    
    def possible_actions(self, actions : set[Action]):
        self.actions = actions
    
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
        
        self.strategies : set[Action] = set()
        
        if nodes and edges: self.graph = Graph(nodes, edges)
        else: self.generate_model()

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
    
    def solve(self) -> set[Edge]:
        if self.budget is None: self.budget = len(self.nodes)

        # Finding the optimal solution with infinite budget
        for n in self.nodes:
            agent = Agent(n)
            while agent.pos != self.target:
                action, possible_actions = agent.choose_action(self)
                self.strategies.add(action) # add the action to the set of strategies
                n.possible_actions(possible_actions) # add the possible actions to the node
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
        if len(self.strategies) > self.budget:
            print("[Found optimal solution with infinite budget, adjusting for given budget...]")
            for n in self.nodes:
                
                  
        
        return self.strat_edges

        
class Agent:
    def __init__(self, pos : Node) -> None:
        self.pos = pos # intial state
    
    def choose_action(self, pomdp : POMDP) -> Action:
        available_actions = pomdp.observe_actions(self.pos)
        expectedMoveValue = {}
        for a in available_actions:
            expectedMoveValue[a] = pomdp.reward(self.pos, a)
        max_value = max(expectedMoveValue.values())
        max_keys = [key for key, value in expectedMoveValue.items() if value == max_value]
        return max(expectedMoveValue, key = lambda k: expectedMoveValue[k]), max_keys
        


if __name__ == '__main__':
    
    # rf = RangeFloat(0.5)  # Initialize with a value
    # print(rf.value)  # Output: 0.5

    # rf.value = 0.7  # Set a new value
    # print(rf.value)  # Output: 0.7

    # rf.value = 1.5  # Trying to set an invalid value
    # # Output: ValueError: Value must be between 0 and 1

    
    pomdp = POMDP(gridSize=(3,3), target=Node(2,2), model='grid')
    print(pomdp.solve())


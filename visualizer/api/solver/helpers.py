from enum import Enum
from copy import deepcopy

import numpy as np
from itertools import combinations

class Action(Enum):
    """
    Enum class for the actions that the agent can take.

    Actions = {UP, RIGHT, DOWN, LEFT}
    """
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    
    def __str__(self):
        # capitalize the first letter of the action while the rest is lowercase
        # return self.name[0] + self.name[1:].lower()
        return self.name[0].lower()
    
    def __repr__(self):
        return self.name[0].lower()

    def __eq__(self, value: object) -> bool:
        return super().__eq__(value)
    
    def __hash__(self) -> int:
        return hash(self.name)
    

class RangeFloat:
    """
    A float that is within the range [0, 1]
    """
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
    """
    A strategy is a mapping from actions to probabilities.
    """
    
    def __init__(self, actions : dict[Action, RangeFloat] = None) -> None:
        self.id = id(self) # unique id
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
    
    # if strategy is subscriptable, return the probability of the action
    def __getitem__(self, action : Action) -> RangeFloat:
        try:
            return self.actions[action]
        except KeyError:
            # if actions is not defined within actions
            # then the startegy does not have will never
            # peform that action
            return RangeFloat(0.0)



class Node:
    """
    A node in the graph. It has a unique identifier on a grid (i, j).
    """
    
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
    
    def __gt__(self, other):
        return self.i > other.i or (self.i == other.i and self.j > other.j)
    
    def assign_strategy(self, strategy : Strategy, strategy_id : int):
        self.strategy = strategy
        self.strategy_id = strategy_id
    
    def set_suitable_actions(self, suitable_actions : set[Action]):
        self.suitable_actions = suitable_actions
        
    
class Edge:
    """
    An edge in the graph. It connects two nodes.
    """
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
    """
    A graph is a collection of nodes and edges. It also provides an adjacency list representation of the graph to facilitate traversal.
    """
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
    
from z3 import Model, Z3_INT_SORT, Z3_REAL_SORT

def Z3Serializer(m : Model) -> dict:
    """
    Convert a Z3 model to a JSON serializable format. Support for int, rational, and string values.

    Args:
        m (Model): a Z3 model
        
    Returns:
        dict: a dictionary representation of the model
    """
    values = {}
    for decl in m.decls():
        if m[decl].sort().kind() == Z3_INT_SORT:
            values[str(decl)] = m[decl].as_long()
        elif m[decl].sort().kind() == Z3_REAL_SORT:
            values[str(decl)] = z3_rational_to_float(m[decl])
        else:
            values[str(decl)] = str(m[decl])
    
    return values

# def z3_model_to_dict(model):
#     """
#     Convert a Z3 model to a dictionary.
#     """
#     result = {}
#     for declaration in model.decls():
#         var = declaration()
#         result[str(var)] = model[var]
#     return result

def z3_rational_to_float(rational):
    return float(rational.numerator_as_long()) / float(rational.denominator_as_long())
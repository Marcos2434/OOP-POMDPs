# REST framework
from rest_framework.response import Response
from rest_framework import status

# Local
from ..serializers import Z3Serializer

# OOP
from OOP.createLine import create_line_constrained
from OOP.createGrid import create_grid_constrained
from OOP.createMaze import create_maze_constrained

from OOP.createLineFixed import create_line_pre
from OOP.createGridFixed import create_grid_pre
from OOP.createMazeFixed import create_maze_pre

import importlib.util

# AI Helpers
from .pomdp import POMDP
from .helpers import Node

def Z3_Solver(data) -> Response:
    if data['model'] == "Line":
        if not 'sensor_selection' in data:
            create_line_constrained(
                target=int(data['target']),
                size=int(data['size']),
                budget=int(data['budget']),
                threshold="<= " + data['threshold'],
                det=bool(data['deterministic']),
            )
            
            if bool(data['deterministic']): module_path = 'OOP/generated_models/' + data['model'].lower() + '_' + data['size'] + '_det_z3.py'
            else: module_path = 'OOP/generated_models/' + data['model'].lower() + '_' + data['size'] + '_ran_z3.py'
        else:
            create_line_pre(
                target=int(data['target']),
                size=int(data['size']),
                budget=int(data['budget']),
                threshold="<= " + data['threshold'],
                det=bool(data['deterministic']),
                pre=data['observables'],
            )
            if bool(data['deterministic']): module_path = 'OOP/generated_models/fixed_line_' + data['size'] + '_det_z3.py'
            else: module_path = 'OOP/generated_models/fixed_line_' + data['size'] + '_ran_z3.py'
            
    elif data['model'] == "Grid":
        if not 'sensor_selection' in data:
            create_grid_constrained(
                target=int(data['target']),
                size=int(data['size']),
                budget=int(data['budget']),
                threshold="<= " + data['threshold'],
                det=bool(data['deterministic']),
            )
            if bool(data['deterministic']): module_path = 'OOP/generated_models/' + data['model'].lower() + '_' + data['size'] + 'x' + data['size'] + '_det_z3.py'
            else: module_path = 'OOP/generated_models/' + data['model'].lower() + '_' + data['size'] + 'x' + data['size'] + '_ran_z3.py'
        else:
            create_grid_pre(
                target=int(data['target']),
                sizex=int(data['size']),
                sizey=int(data['size']),
                budget=int(data['budget']),
                threshold="<= " + data['threshold'],
                det=bool(data['deterministic']),
                pre=data['observables'],
            )
            if bool(data['deterministic']): module_path = 'OOP/generated_models/fixed_grid_' + data['size'] + 'x' + data['size'] + 'det_z3.py'
            else: module_path = 'OOP/generated_models/fixed_grid_' + data['size'] + 'x' + data['size'] + '_ran_z3.py'
            
    elif data['model'] == "Maze":
        if not 'sensor_selection' in data:
            create_maze_constrained(
                budget = int(data['budget']),
                target = int(data['target']),
                sizex = int(data['rows']), 
                sizey = int(data['columns']), 
                threshold="<= " + data['threshold'],
                det = bool(data['deterministic'])
            )
            if bool(data['deterministic']): module_path = 'OOP/generated_models/' + data['model'].lower() + '_' + data['rows'] + 'x' + data['columns'] + '_det_z3.py'
            else: module_path = 'OOP/generated_models/' + data['model'].lower() + '_' + data['rows'] + 'x' + data['columns'] + '_ran_z3.py'
        else:
            create_maze_pre(
                budget = int(data['budget']),
                target = int(data['target']),
                sizex = int(data['rows']), 
                sizey = int(data['columns']), 
                threshold="<= " + data['threshold'],
                det = bool(data['deterministic']),
                pre = data['observables']
            )
            if bool(data['deterministic']): module_path = 'OOP/generated_models/fixed_maze_' + data['rows'] + 'x' + data['columns'] + '_det_z3.py'
            else: module_path = 'OOP/generated_models/fixed_maze_' + data['rows'] + 'x' + data['columns'] + '_ran_z3.py'
            
    # import module
    spec = importlib.util.spec_from_file_location("generated_module", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    sol = module.sol()
    if sol == "No Solution":
        return Response({
            'solution' : 'No solution'
        },
        status=status.HTTP_200_OK)
    elif sol == None:
        return Response({
            'solution' : 'Unknown'
        }, status=status.HTTP_200_OK)

    content = {
        'budget' : data['budget'],
        'target' : data['target'],
        'size' : data['size'],
        'threshold' : data['threshold'],
        'deterministic' : True if data['deterministic'] else False,
        'sensor_selection' : True if 'sensor_selection' in data else False,
        'solution': Z3Serializer(sol),
    }
    
    return Response(content, status=status.HTTP_200_OK)

def Brute_Force_Solver(data) -> Response:

    if data['model'] == "Grid":
        gridSize = (int(data['size']), int(data['size']))
        
        # translation layer
        def translate_grid_id_to_grid_coords(gridSize : tuple[int, int], id : int) -> Node:
            return Node(id // gridSize[0], id % gridSize[0])
        
        pomdp = POMDP(
            gridSize=gridSize, 
            model='grid', 
            budget=int(data['budget']),
            target= translate_grid_id_to_grid_coords(gridSize, int(data['target'])),
        )
        
        infinite_budget_optimal_solution, minimal_budget_optimal_solution = pomdp.solve()
        
        
        content = {
            'budget' : data['budget'],
            'target' : data['target'],
            'size' : data['size'],
            'threshold' : data['threshold'],
            'deterministic' : True if data['deterministic'] else False,
            'sensor_selection' : True if 'sensor_selection' in data else False,
            'solution': None,
        }
        
        if minimal_budget_optimal_solution is None:
            if infinite_budget_optimal_solution is None:
                return Response({ 'solution' : 'No solution' }, status=status.HTTP_200_OK)
            else:
                content['solution'] = infinite_budget_optimal_solution
                return Response(content, status=status.HTTP_200_OK)
        else:
            content['solution'] = minimal_budget_optimal_solution['parsed_pomdp']
            return Response(content, status=status.HTTP_200_OK)
    
    # Model not implemented
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)    
    
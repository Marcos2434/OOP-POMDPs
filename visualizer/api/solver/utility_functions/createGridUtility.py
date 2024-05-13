#!/usr/bin/python3
import more_itertools as mit
import sys
import os
import itertools
import math
from six.moves import input
from itertools import chain, combinations
import importlib.util


# prevent .pyc (python cache) files from generating since we are reusing
# the same file name to generate the new file
import sys
sys.dont_write_bytecode = True

FILE_PATH_FLAG = True

if FILE_PATH_FLAG:
    # Run directly
    from helpers import *
    DIR_PATH = '/Users/marcos/Documents/github_projects/POMDPs/visualizer/api/solver/utility_functions/generated_models/'
else:
    # Run through server (Django)
    from ..helpers import *
    DIR_PATH = os.getcwd() + '/api/solver/utility_functions/generated_models/'


def find_latest_file(directory, base_filename):
    """Find the latest file with the base filename."""
    files = [f for f in os.listdir(directory) if f.startswith(base_filename)]
    if files:
        latest_file = max(files)
        index = int(latest_file.split("[")[1].split("]")[0])
        return index
    else: return 0

def generate_next_filename(directory, base_filename):
    """Generate the next filename."""
    latest_index = find_latest_file(directory, base_filename)
    next_index = latest_index + 1
    return f"{base_filename}[{next_index}].py"

def grid_utility(budget, target, size, strategies : dict[int, Strategy], observations : dict[Node, int], det = 0):

    # import os
    # print(os.getcwd())
    # print(os.path.exists(os.getcwd() + '/api/solver/utility_functions/generated_models/grid.py'))
    
    # remove file if it exists 
    # if os.path.exists(FILE_PATH): os.remove(FILE_PATH)
    
    # filename = generate_next_filename(DIR_PATH, "grid")
    # file_path = DIR_PATH + filename
    # file = open(file_path, 'w')
    
    filename = "grid.py"
    file_path = DIR_PATH + filename
    file = open(file_path, 'w')

    file.write('from z3 import *\n\n')
    
    # [MODIFIED]
    file.write("exp = Real('exp')\n")

    side = size

    # Dictionary to keep the values
    var = {}

    actions = ['l', 'r', 'u', 'd']

    column = target % size

    size = size * size

    file.write('# Expected cost/reward of reaching the goal.\n')
    for i in range(0, size):
        file.write('pi' + str(i) + ' = Real(\'pi' + str(i) + '\')\n')


    file.write('\n# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)\n')
    for i in range(0, size):
        # if i == target:
        #     continue
        for j in range(1, budget + 1):
            file.write('ys' + str(i) + "_" + str(j) + ' = Real(\'ys' + str(i) + "_" + str(j) + '\')\n')


    file.write('\n# Rates of randomized strategies\n')
    for i in range(1, budget + 1):
        file.write('xo' + str(i) + 'l' + ' = Real(\'xo' + str(i) + 'l\')\n')
        file.write('xo' + str(i) + 'r' + ' = Real(\'xo' + str(i) + 'r\')\n')
        file.write('xo' + str(i) + 'u' + ' = Real(\'xo' + str(i) + 'u\')\n')
        file.write('xo' + str(i) + 'd' + ' = Real(\'xo' + str(i) + 'd\')\n')


    file.write('solver = Solver()\n\n\n')

    file.write('solver.add(\n')

    file.write('#We cannot do better than the fully observable case\n')

    count = 0

    for i in range(0, size):
        if i%target == column:
            file.write('pi' + str(i) + '>=' + str(abs(target - i)//side) + ', ')
            count = count + abs(target - i)//side
        else:
            file.write('pi' + str(i) + '>=' + str(abs(column - i%side) + (abs(target - i)//side)) + ', ')
            count = count + abs(column - i%side) + (abs(target - i)//side)
    file.write('\n# Expected cost/reard equations\n')

    #If you print count, you can find the optimal reward.
    #print(count)



    for i in range(0, size):
        left = ''
        right = ''
        up = ''
        down = ''
        if i == target:
            file.write('pi' + str(i) + ' == 0, \n')
            continue
        file.write('pi' + str(i) + ' == ' + '(')

        for o in range(1, budget+1):
            if o < budget:
                left = left + 'ys' + str(i) + "_" + str(o) + '*xo' + str(o) + 'l + '
                right = right + 'ys' + str(i) + "_" + str(o) + '*xo' + str(o) + 'r + '
                up = up + 'ys' + str(i) + "_" + str(o) + '*xo' + str(o) + 'u + '
                down = down + 'ys' + str(i) + "_" + str(o) + '*xo' + str(o) + 'd + '
            else:
                if i%side == 0:
                    left = left + 'ys' + str(i) + "_" + str(o) + '*xo' + str(o) + 'l) * (1 + pi' + str(i) + ') + ('
                else: 
                    left = left + 'ys' + str(i) + "_" + str(o) + '*xo' + str(o) + 'l) * (1 + pi' + str(i - 1) + ') + ('
                if i%side == side-1:
                    right = right + 'ys' + str(i) + "_" + str(o) + '*xo' + str(o) + 'r) * (1 + pi' + str(i) + ') + ('
                else: 
                    right = right + 'ys' + str(i) + "_" + str(o) + '*xo' + str(o) + 'r) * (1 + pi' + str(i + 1) + ') + ('
                if i - side >=0:
                    up = up + 'ys' + str(i) + "_" + str(o) + '*xo' + str(o) + 'u) * (1 + pi' + str(i - side) + ') + ('
                else: 
                    up = up + 'ys' + str(i) + "_" + str(o) + '*xo' + str(o) + 'u) * (1 + pi' + str(i) + ') + ('
                if i + side < size:
                    down = down + 'ys' + str(i) + "_" + str(o) + '*xo' + str(o) + 'd) * (1 + pi' + str(i + side) + '),\n'
                else: 
                    down = down + 'ys' + str(i) + "_" + str(o) + '*xo' + str(o) + 'd) * (1 + pi' + str(i) + '),\n'
        file.write(left + right + up + down)

    # [MODIFIED (no threshold)]
    # file.write('# We are dropped uniformly in the grid\n# We want to check if the minimal expected cost is below some threshold ' + str(threshold) + '\n')

    line = '('
    for i in range(0, size):
        if i == target:
            continue
        if i < size - 1:
            if target == size - 1:
                if i == size - 2 :
                    line = line + 'pi' + str(i) + ')'
                else:
                    line = line + 'pi' + str(i) + '+'
            else:
                line = line + 'pi' + str(i) + '+'
        else:
            line = line + 'pi' + str(i) + ')'
    # [MODIFIED (no threshold)]
    line = 'exp==(' + line + ') * Q(1,' + str(size-1) + ')' + ','

    file.write(line + '\n')

    file.write('# Randomised strategies (proper probability distributions)\n')
    for i in range(1, budget + 1):
        for a in actions:
            file.write('xo' + str(i) + a + '>= 0,\n')
            file.write('xo' + str(i) + a + '<= 1,\n')
    
    # [MODIFIED]
    file.write('# Assigning the action probability distribution from the strategies\n')
    for id, s in strategies.items():
        for a in Action:
            z3rational = 'Q(' + str(s[a].numerator) + ', ' + str(s[a].denominator) + ')'
            file.write(f'xo{id}{a}== {z3rational},\n')
            
    # for i, s in strategies:
    #     i += 1 # 1-indexed strategies
    #     for a in Action:
    #         file.write('xo' + str(i) + str(a) + '== ' + str(s[a]) + ',\n')



    for i in range(1, budget + 1):
        for a in Action:
            if a != Action.LEFT:
                file.write('xo' + str(i) + str(a) + ' + ')
            else:
                file.write('xo' + str(i) + str(a) + ' == 1,\n')

    if det == 1:
        file.write('# Deterministic Strategies activated\n')
        for i in range(1, budget + 1):
            file.write('Or(xo' + str(i) + 'l ' + '== 0, xo' + str(i) + 'l' + ' == 1),\n')
            file.write('Or(xo' + str(i) + 'r ' + '== 0, xo' + str(i) + 'r' + ' == 1),\n')
            file.write('Or(xo' + str(i) + 'u ' + '== 0, xo' + str(i) + 'u' + ' == 1),\n')
            file.write('Or(xo' + str(i) + 'd ' + '== 0, xo' + str(i) + 'd' + ' == 1),\n')

    # [MODIFIED]
    # file.write('# ysNM is a function that should map every state N to some observable class M\n')
    # for i in range(0, size):
    #     if i == target:
    #         continue
    #     for j in range(1, budget + 1):
    #         file.write('Or(ys' + str(i) + "_" + str(j) +  '== 0 , ys' + str(i) + "_" + str(j) + '== 1),\n')

    
    # We know the the observables assigned to each state 
    # from the assignments parameter, so we can write 
    # them directly to the file
    file.write("# Assigned observables\n")
    for n, s_id in observations.items():
        file.write(f'ys{n.id}_{s_id} == 1,\n')
        for i in range(1, budget + 1):
            if i != s_id:
                file.write(f'ys{n.id}_{i} == 0,\n')
    
    # [MODIFIED]
    file.write('# Every state should be mapped to exactly one equivalence class\n')
    
    for i in range(0, size):
        if i == target:
            continue
        for j in range(1, budget + 1):
            file.write('ys' + str(i) + "_" + str(j))
            if j < budget:
                file.write(' + ')
            else:
                file.write(' == 1')
        if i == size - 1:
            file.write('\n)\n\n')
        else:
            if target == size - 1:
                if i == size - 2:
                    file.write('\n)\n\n')
                else:
                    file.write(',\n')
            else:
                file.write(',\n')
    
    # [MODIFIED] 
    # file.write('if solver.check() == sat:\n\t')
    # file.write('m = solver.model()\n\t')
    # file.write('print(\'This is a solution:\')\n\t')
    # file.write('print(m)\n')
    # file.write('elif solver.check() == unsat:\n\t')
    # file.write('print(\'No solution!!!\')\n')
    # file.write('else:\n\t')
    # file.write('print(\'Unknown\')')
    
    # [MODIFIED] 
    file.write('\nsol = lambda : solver.model() if solver.check() == sat else "No Solution" if solver.check() == unsat else None')
    file.close()
    
    # import generated python file and get the function "sol"
    spec = importlib.util.spec_from_file_location("generated_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # ModelRef to python dict
    model = module.sol()

    if model == "No Solution" or model is None: return 0, None
    model = Z3Serializer(model)
    return float(model['exp']), model

    # return module.sol()

# size = int(sys.argv[1])
# target = int(sys.argv[2])
# budget = int(sys.argv[3])
# threshold = sys.argv[4]
# det = int(sys.argv[5])


# create_grid_constrained(budget, target, size, threshold, det)

# create_grid_constrained(budget=2, target=3, size=3)
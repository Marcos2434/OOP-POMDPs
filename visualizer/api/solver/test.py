from itertools import combinations
from helpers import Strategy, Action

used_actions = set([Action.DOWN, Action.RIGHT])

# strategies : set[Action] = set()
# for i in range(len(used_actions)):
#     strategies |= set(combinations(used_actions, i+1))
    
strategies : set[Action] = set()
for i in range(len(used_actions)):
    # strategies |= set(combinations(used_actions, i+1))
    for comb in set(combinations(used_actions, i+1)):
        strategies.add(Strategy(actions = {action: 1 / (i+1) for action in comb}))
        
print(strategies)

strategy_combinations = set()
B = 2
for i in range(B):
    strategy_combinations |= set(combinations(strategies, i+1))

print(strategy_combinations)


# available_strategy_combinations = set()
# for i in range(1, self.budget+1):
#     available_strategy_combinations.update(set(combinations(possible_strategies, i)))

from z3 import *

# Expected cost/reward of reaching the goal.
pi0 = Real('pi0')
pi1 = Real('pi1')
pi2 = Real('pi2')
pi3 = Real('pi3')
pi4 = Real('pi4')

# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)
ys0_1 = Real('ys0_1')
ys0_2 = Real('ys0_2')
ys1_1 = Real('ys1_1')
ys1_2 = Real('ys1_2')
ys3_1 = Real('ys3_1')
ys3_2 = Real('ys3_2')
ys4_1 = Real('ys4_1')
ys4_2 = Real('ys4_2')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=2, pi1>=1, pi2>=0, pi3>=1, pi4>=2, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l+ ys0_2*xo2l)*(1 + pi0) + (ys0_1*xo1r+ ys0_2*xo2r)*(1 + pi1),
pi1 == (ys1_1*xo1l+ ys1_2*xo2l)*(1 + pi0) + (ys1_1*xo1r+ ys1_2*xo2r)*(1 + pi2),
pi2 == 0, 
pi3 == (ys3_1*xo1l+ ys3_2*xo2l)*(1 + pi2) + (ys3_1*xo1r+ ys3_2*xo2r)*(1 + pi4),
pi4 == (ys4_1*xo1l+ ys4_2*xo2l)*(1 + pi3) + (ys4_1*xo1r+ ys4_2*xo2r)*(1 + pi4),
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= 2.25
(pi0+pi1+pi3+pi4) * Q(1,4) <= 2.25,
# Randomised strategies (proper probability distributions)
xo1l>= 0,
xo1l<= 1,
xo1r>= 0,
xo1r<= 1,
xo2l>= 0,
xo2l<= 1,
xo2r>= 0,
xo2r<= 1,
xo1l + xo1r == 1,
xo2l + xo2r == 1,
# Deterministic Strategies activated
Or(xo1l == 0, xo1l == 1),
Or(xo1r == 0, xo1r == 1),
Or(xo2l == 0, xo2l == 1),
Or(xo2r == 0, xo2r == 1),
# ysNM is a function that should map every state N to some observable class M
Or(ys0_1== 0 , ys0_1== 1),
Or(ys0_2== 0 , ys0_2== 1),
Or(ys1_1== 0 , ys1_1== 1),
Or(ys1_2== 0 , ys1_2== 1),
Or(ys3_1== 0 , ys3_1== 1),
Or(ys3_2== 0 , ys3_2== 1),
Or(ys4_1== 0 , ys4_1== 1),
Or(ys4_2== 0 , ys4_2== 1),
# Every state should be mapped to exactly one equivalence class
ys0_1 + ys0_2 == 1,
ys1_1 + ys1_2 == 1,
ys3_1 + ys3_2 == 1,
ys4_1 + ys4_2 == 1
)

if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')
sol = lambda : solver.model() if solver.check() == sat else "No Solution" if solver.check() == unsat else None
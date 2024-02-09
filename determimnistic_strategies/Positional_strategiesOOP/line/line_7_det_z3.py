from z3 import *

# Expected cost/reward of reaching the goal.
pi0 = Real('pi0')
pi1 = Real('pi1')
pi2 = Real('pi2')
pi3 = Real('pi3')
pi4 = Real('pi4')
pi5 = Real('pi5')
pi6 = Real('pi6')

# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)
ys01 = Real('ys01')
ys02 = Real('ys02')
ys11 = Real('ys11')
ys12 = Real('ys12')
ys21 = Real('ys21')
ys22 = Real('ys22')
ys41 = Real('ys41')
ys42 = Real('ys42')
ys51 = Real('ys51')
ys52 = Real('ys52')
ys61 = Real('ys61')
ys62 = Real('ys62')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=3, pi1>=2, pi2>=1, pi3>=0, pi4>=1, pi5>=2, pi6>=3, 
# Expected cost/reard equations
pi0 == (ys01*xo1l+ ys02*xo2l)*(1 + pi0) + (ys01*xo1r+ ys02*xo2r)*(1 + pi1),
pi1 == (ys11*xo1l+ ys12*xo2l)*(1 + pi0) + (ys11*xo1r+ ys12*xo2r)*(1 + pi2),
pi2 == (ys21*xo1l+ ys22*xo2l)*(1 + pi1) + (ys21*xo1r+ ys22*xo2r)*(1 + pi3),
pi3 == 0, 
pi4 == (ys41*xo1l+ ys42*xo2l)*(1 + pi3) + (ys41*xo1r+ ys42*xo2r)*(1 + pi5),
pi5 == (ys51*xo1l+ ys52*xo2l)*(1 + pi4) + (ys51*xo1r+ ys52*xo2r)*(1 + pi6),
pi6 == (ys61*xo1l+ ys62*xo2l)*(1 + pi5) + (ys61*xo1r+ ys62*xo2r)*(1 + pi6),
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= 2
(pi0+pi1+pi2+pi4+pi5+pi6) * Q(1,6) <= 2,
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
Or(ys01== 0 , ys01== 1),
Or(ys02== 0 , ys02== 1),
Or(ys11== 0 , ys11== 1),
Or(ys12== 0 , ys12== 1),
Or(ys21== 0 , ys21== 1),
Or(ys22== 0 , ys22== 1),
Or(ys41== 0 , ys41== 1),
Or(ys42== 0 , ys42== 1),
Or(ys51== 0 , ys51== 1),
Or(ys52== 0 , ys52== 1),
Or(ys61== 0 , ys61== 1),
Or(ys62== 0 , ys62== 1),
# Every state should be mapped to exactly one equivalence class
ys01 + ys02 == 1,
ys11 + ys12 == 1,
ys21 + ys22 == 1,
ys41 + ys42 == 1,
ys51 + ys52 == 1,
ys61 + ys62 == 1
)

if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')
from z3 import *

# Expected cost/reward of reaching the goal.
pi0 = Real('pi0')
pi1 = Real('pi1')
pi2 = Real('pi2')
pi3 = Real('pi3')

# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)
ys01 = Real('ys01')
ys02 = Real('ys02')
ys11 = Real('ys11')
ys12 = Real('ys12')
ys21 = Real('ys21')
ys22 = Real('ys22')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo1u = Real('xo1u')
xo1d = Real('xo1d')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
xo2u = Real('xo2u')
xo2d = Real('xo2d')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=2, pi1>=1, pi2>=1, pi3>=0, 
# Expected cost/reard equations
pi0 == (ys01*xo1l + ys02*xo2l) * (1 + pi0) + (ys01*xo1r + ys02*xo2r) * (1 + pi1) + (ys01*xo1u + ys02*xo2u) * (1 + pi0) + (ys01*xo1d + ys02*xo2d) * (1 + pi2),
pi1 == (ys11*xo1l + ys12*xo2l) * (1 + pi0) + (ys11*xo1r + ys12*xo2r) * (1 + pi1) + (ys11*xo1u + ys12*xo2u) * (1 + pi1) + (ys11*xo1d + ys12*xo2d) * (1 + pi3),
pi2 == (ys21*xo1l + ys22*xo2l) * (1 + pi2) + (ys21*xo1r + ys22*xo2r) * (1 + pi3) + (ys21*xo1u + ys22*xo2u) * (1 + pi0) + (ys21*xo1d + ys22*xo2d) * (1 + pi2),
pi3 == 0, 
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= 1.5
(pi0+pi1+pi2) * Q(1,3) <= 1.5,
# Randomised strategies (proper probability distributions)
xo1l>= 0,
xo1l<= 1,
xo1r>= 0,
xo1r<= 1,
xo1u>= 0,
xo1u<= 1,
xo1d>= 0,
xo1d<= 1,
xo2l>= 0,
xo2l<= 1,
xo2r>= 0,
xo2r<= 1,
xo2u>= 0,
xo2u<= 1,
xo2d>= 0,
xo2d<= 1,
xo1l + xo1r + xo1u + xo1d == 1,
xo2l + xo2r + xo2u + xo2d == 1,
# Deterministic Strategies activated
Or(xo1l == 0, xo1l == 1),
Or(xo1r == 0, xo1r == 1),
Or(xo1u == 0, xo1u == 1),
Or(xo1d == 0, xo1d == 1),
Or(xo2l == 0, xo2l == 1),
Or(xo2r == 0, xo2r == 1),
Or(xo2u == 0, xo2u == 1),
Or(xo2d == 0, xo2d == 1),
# ysNM is a function that should map every state N to some observable class M
Or(ys01== 0 , ys01== 1),
Or(ys02== 0 , ys02== 1),
Or(ys11== 0 , ys11== 1),
Or(ys12== 0 , ys12== 1),
Or(ys21== 0 , ys21== 1),
Or(ys22== 0 , ys22== 1),
# Every state should be mapped to exactly one equivalence class
ys01 + ys02 == 1,
ys11 + ys12 == 1,
ys21 + ys22 == 1
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
from z3 import *

# Expected cost/reward of reaching the goal.
pi0 = Real('pi0')
pi1 = Real('pi1')
pi2 = Real('pi2')
pi3 = Real('pi3')
pi4 = Real('pi4')
pi5 = Real('pi5')
pi6 = Real('pi6')
pi7 = Real('pi7')

# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)
ys01 = Real('ys01')
ys02 = Real('ys02')
ys11 = Real('ys11')
ys12 = Real('ys12')
ys21 = Real('ys21')
ys22 = Real('ys22')
ys31 = Real('ys31')
ys32 = Real('ys32')
ys51 = Real('ys51')
ys52 = Real('ys52')
ys61 = Real('ys61')
ys62 = Real('ys62')
ys71 = Real('ys71')
ys72 = Real('ys72')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=4, pi1>=3, pi2>=2, pi3>=1, pi4>=0, pi5>=1, pi6>=2, pi7>=3, 
# Expected cost/reard equations
pi0 == (ys01*xo1l+ ys02*xo2l)*(1 + pi0) + (ys01*xo1r+ ys02*xo2r)*(1 + pi1),
pi1 == (ys11*xo1l+ ys12*xo2l)*(1 + pi0) + (ys11*xo1r+ ys12*xo2r)*(1 + pi2),
pi2 == (ys21*xo1l+ ys22*xo2l)*(1 + pi1) + (ys21*xo1r+ ys22*xo2r)*(1 + pi3),
pi3 == (ys31*xo1l+ ys32*xo2l)*(1 + pi2) + (ys31*xo1r+ ys32*xo2r)*(1 + pi4),
pi4 == 0, 
pi5 == (ys51*xo1l+ ys52*xo2l)*(1 + pi4) + (ys51*xo1r+ ys52*xo2r)*(1 + pi6),
pi6 == (ys61*xo1l+ ys62*xo2l)*(1 + pi5) + (ys61*xo1r+ ys62*xo2r)*(1 + pi7),
pi7 == (ys71*xo1l+ ys72*xo2l)*(1 + pi6) + (ys71*xo1r+ ys72*xo2r)*(1 + pi7),
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= 100
(pi0+pi1+pi2+pi3+pi5+pi6+pi7) * Q(1,7) <= 100,
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
# ysNM is a function that should map every state N to some observable class M
Or(ys01== 0 , ys01== 1),
Or(ys02== 0 , ys02== 1),
Or(ys11== 0 , ys11== 1),
Or(ys12== 0 , ys12== 1),
Or(ys21== 0 , ys21== 1),
Or(ys22== 0 , ys22== 1),
Or(ys31== 0 , ys31== 1),
Or(ys32== 0 , ys32== 1),
Or(ys51== 0 , ys51== 1),
Or(ys52== 0 , ys52== 1),
Or(ys61== 0 , ys61== 1),
Or(ys62== 0 , ys62== 1),
Or(ys71== 0 , ys71== 1),
Or(ys72== 0 , ys72== 1),
# Every state should be mapped to exactly one equivalence class
ys01 + ys02 == 1,
ys11 + ys12 == 1,
ys21 + ys22 == 1,
ys31 + ys32 == 1,
ys51 + ys52 == 1,
ys61 + ys62 == 1,
ys71 + ys72 == 1
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
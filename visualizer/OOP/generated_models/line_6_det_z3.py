from z3 import *

# Expected cost/reward of reaching the goal.
pi0 = Real('pi0')
pi1 = Real('pi1')
pi2 = Real('pi2')
pi3 = Real('pi3')
pi4 = Real('pi4')
pi5 = Real('pi5')

# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)
ys01 = Real('ys01')
ys02 = Real('ys02')
ys03 = Real('ys03')
ys11 = Real('ys11')
ys12 = Real('ys12')
ys13 = Real('ys13')
ys31 = Real('ys31')
ys32 = Real('ys32')
ys33 = Real('ys33')
ys41 = Real('ys41')
ys42 = Real('ys42')
ys43 = Real('ys43')
ys51 = Real('ys51')
ys52 = Real('ys52')
ys53 = Real('ys53')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
xo3l = Real('xo3l')
xo3r = Real('xo3r')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=2, pi1>=1, pi2>=0, pi3>=1, pi4>=2, pi5>=3, 
# Expected cost/reard equations
pi0 == (ys01*xo1l+ ys02*xo2l+ ys03*xo3l)*(1 + pi0) + (ys01*xo1r+ ys02*xo2r+ ys03*xo3r)*(1 + pi1),
pi1 == (ys11*xo1l+ ys12*xo2l+ ys13*xo3l)*(1 + pi0) + (ys11*xo1r+ ys12*xo2r+ ys13*xo3r)*(1 + pi2),
pi2 == 0, 
pi3 == (ys31*xo1l+ ys32*xo2l+ ys33*xo3l)*(1 + pi2) + (ys31*xo1r+ ys32*xo2r+ ys33*xo3r)*(1 + pi4),
pi4 == (ys41*xo1l+ ys42*xo2l+ ys43*xo3l)*(1 + pi3) + (ys41*xo1r+ ys42*xo2r+ ys43*xo3r)*(1 + pi5),
pi5 == (ys51*xo1l+ ys52*xo2l+ ys53*xo3l)*(1 + pi4) + (ys51*xo1r+ ys52*xo2r+ ys53*xo3r)*(1 + pi5),
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= 1.5
(pi0+pi1+pi3+pi4+pi5) * Q(1,5) <= 1.5,
# Randomised strategies (proper probability distributions)
xo1l>= 0,
xo1l<= 1,
xo1r>= 0,
xo1r<= 1,
xo2l>= 0,
xo2l<= 1,
xo2r>= 0,
xo2r<= 1,
xo3l>= 0,
xo3l<= 1,
xo3r>= 0,
xo3r<= 1,
xo1l + xo1r == 1,
xo2l + xo2r == 1,
xo3l + xo3r == 1,
# ysNM is a function that should map every state N to some observable class M
Or(ys01== 0 , ys01== 1),
Or(ys02== 0 , ys02== 1),
Or(ys03== 0 , ys03== 1),
Or(ys11== 0 , ys11== 1),
Or(ys12== 0 , ys12== 1),
Or(ys13== 0 , ys13== 1),
Or(ys31== 0 , ys31== 1),
Or(ys32== 0 , ys32== 1),
Or(ys33== 0 , ys33== 1),
Or(ys41== 0 , ys41== 1),
Or(ys42== 0 , ys42== 1),
Or(ys43== 0 , ys43== 1),
Or(ys51== 0 , ys51== 1),
Or(ys52== 0 , ys52== 1),
Or(ys53== 0 , ys53== 1),
# Every state should be mapped to exactly one equivalence class
ys01 + ys02 + ys03 == 1,
ys11 + ys12 + ys13 == 1,
ys31 + ys32 + ys33 == 1,
ys41 + ys42 + ys43 == 1,
ys51 + ys52 + ys53 == 1
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
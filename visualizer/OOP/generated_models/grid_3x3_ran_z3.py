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
pi8 = Real('pi8')

# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)
ys0_1 = Real('ys0_1')
ys1_1 = Real('ys1_1')
ys2_1 = Real('ys2_1')
ys3_1 = Real('ys3_1')
ys4_1 = Real('ys4_1')
ys5_1 = Real('ys5_1')
ys6_1 = Real('ys6_1')
ys7_1 = Real('ys7_1')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo1u = Real('xo1u')
xo1d = Real('xo1d')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=4, pi1>=3, pi2>=2, pi3>=3, pi4>=2, pi5>=1, pi6>=2, pi7>=1, pi8>=0, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l) * (1 + pi0) + (ys0_1*xo1r) * (1 + pi1) + (ys0_1*xo1u) * (1 + pi0) + (ys0_1*xo1d) * (1 + pi3),
pi1 == (ys1_1*xo1l) * (1 + pi0) + (ys1_1*xo1r) * (1 + pi2) + (ys1_1*xo1u) * (1 + pi1) + (ys1_1*xo1d) * (1 + pi4),
pi2 == (ys2_1*xo1l) * (1 + pi1) + (ys2_1*xo1r) * (1 + pi2) + (ys2_1*xo1u) * (1 + pi2) + (ys2_1*xo1d) * (1 + pi5),
pi3 == (ys3_1*xo1l) * (1 + pi3) + (ys3_1*xo1r) * (1 + pi4) + (ys3_1*xo1u) * (1 + pi0) + (ys3_1*xo1d) * (1 + pi6),
pi4 == (ys4_1*xo1l) * (1 + pi3) + (ys4_1*xo1r) * (1 + pi5) + (ys4_1*xo1u) * (1 + pi1) + (ys4_1*xo1d) * (1 + pi7),
pi5 == (ys5_1*xo1l) * (1 + pi4) + (ys5_1*xo1r) * (1 + pi5) + (ys5_1*xo1u) * (1 + pi2) + (ys5_1*xo1d) * (1 + pi8),
pi6 == (ys6_1*xo1l) * (1 + pi6) + (ys6_1*xo1r) * (1 + pi7) + (ys6_1*xo1u) * (1 + pi3) + (ys6_1*xo1d) * (1 + pi6),
pi7 == (ys7_1*xo1l) * (1 + pi6) + (ys7_1*xo1r) * (1 + pi8) + (ys7_1*xo1u) * (1 + pi4) + (ys7_1*xo1d) * (1 + pi7),
pi8 == 0, 
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= 10
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7) * Q(1,8) <= 10,
# Randomised strategies (proper probability distributions)
xo1l>= 0,
xo1l<= 1,
xo1r>= 0,
xo1r<= 1,
xo1u>= 0,
xo1u<= 1,
xo1d>= 0,
xo1d<= 1,
xo1l + xo1r + xo1u + xo1d == 1,
# ysNM is a function that should map every state N to some observable class M
Or(ys0_1== 0 , ys0_1== 1),
Or(ys1_1== 0 , ys1_1== 1),
Or(ys2_1== 0 , ys2_1== 1),
Or(ys3_1== 0 , ys3_1== 1),
Or(ys4_1== 0 , ys4_1== 1),
Or(ys5_1== 0 , ys5_1== 1),
Or(ys6_1== 0 , ys6_1== 1),
Or(ys7_1== 0 , ys7_1== 1),
# Every state should be mapped to exactly one equivalence class
ys0_1 == 1,
ys1_1 == 1,
ys2_1 == 1,
ys3_1 == 1,
ys4_1 == 1,
ys5_1 == 1,
ys6_1 == 1,
ys7_1 == 1
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
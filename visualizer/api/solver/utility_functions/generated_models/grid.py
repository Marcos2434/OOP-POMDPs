from z3 import *

exp = Real('exp')
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
ys5_1 = Real('ys5_1')
ys6_1 = Real('ys6_1')
ys7_1 = Real('ys7_1')
ys8_1 = Real('ys8_1')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo1u = Real('xo1u')
xo1d = Real('xo1d')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=2, pi1>=1, pi2>=1, pi3>=1, pi4>=0, pi5>=0, pi6>=1, pi7>=1, pi8>=2, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l) * (1 + pi0) + (ys0_1*xo1r) * (1 + pi1) + (ys0_1*xo1u) * (1 + pi0) + (ys0_1*xo1d) * (1 + pi3),
pi1 == (ys1_1*xo1l) * (1 + pi0) + (ys1_1*xo1r) * (1 + pi2) + (ys1_1*xo1u) * (1 + pi1) + (ys1_1*xo1d) * (1 + pi4),
pi2 == (ys2_1*xo1l) * (1 + pi1) + (ys2_1*xo1r) * (1 + pi2) + (ys2_1*xo1u) * (1 + pi2) + (ys2_1*xo1d) * (1 + pi5),
pi3 == (ys3_1*xo1l) * (1 + pi3) + (ys3_1*xo1r) * (1 + pi4) + (ys3_1*xo1u) * (1 + pi0) + (ys3_1*xo1d) * (1 + pi6),
pi4 == 0, 
pi5 == (ys5_1*xo1l) * (1 + pi4) + (ys5_1*xo1r) * (1 + pi5) + (ys5_1*xo1u) * (1 + pi2) + (ys5_1*xo1d) * (1 + pi8),
pi6 == (ys6_1*xo1l) * (1 + pi6) + (ys6_1*xo1r) * (1 + pi7) + (ys6_1*xo1u) * (1 + pi3) + (ys6_1*xo1d) * (1 + pi6),
pi7 == (ys7_1*xo1l) * (1 + pi6) + (ys7_1*xo1r) * (1 + pi8) + (ys7_1*xo1u) * (1 + pi4) + (ys7_1*xo1d) * (1 + pi7),
pi8 == (ys8_1*xo1l) * (1 + pi7) + (ys8_1*xo1r) * (1 + pi8) + (ys8_1*xo1u) * (1 + pi5) + (ys8_1*xo1d) * (1 + pi8),
exp==((pi0+pi1+pi2+pi3+pi5+pi6+pi7+pi8)) * Q(1,8),
# Randomised strategies (proper probability distributions)
xo1l>= 0,
xo1l<= 1,
xo1r>= 0,
xo1r<= 1,
xo1u>= 0,
xo1u<= 1,
xo1d>= 0,
xo1d<= 1,
# Randomised strategies (proper probability distributions)
xo1u== 0.3333333333333333,
xo1r== 0.3333333333333333,
xo1d== 0.0,
xo1l== 0.3333333333333333,
xo1u + xo1r + xo1d + xo1l == 1,
# Assigned observables
ys1_1 == 1,
ys5_1 == 1,
ys7_1 == 1,
ys0_1 == 1,
ys6_1 == 1,
ys2_1 == 1,
ys8_1 == 1,
ys3_1 == 1,
# Every state should be mapped to exactly one equivalence class
ys0_1 == 1,
ys1_1 == 1,
ys2_1 == 1,
ys3_1 == 1,
ys5_1 == 1,
ys6_1 == 1,
ys7_1 == 1,
ys8_1 == 1
)


sol = lambda : solver.model() if solver.check() == sat else "No Solution" if solver.check() == unsat else None
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
pi9 = Real('pi9')
pi10 = Real('pi10')
pi11 = Real('pi11')
pi12 = Real('pi12')
pi13 = Real('pi13')
pi14 = Real('pi14')
pi15 = Real('pi15')

# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)
ys0_1 = Real('ys0_1')
ys1_1 = Real('ys1_1')
ys2_1 = Real('ys2_1')
ys3_1 = Real('ys3_1')
ys4_1 = Real('ys4_1')
ys5_1 = Real('ys5_1')
ys6_1 = Real('ys6_1')
ys7_1 = Real('ys7_1')
ys8_1 = Real('ys8_1')
ys9_1 = Real('ys9_1')
ys10_1 = Real('ys10_1')
ys11_1 = Real('ys11_1')
ys12_1 = Real('ys12_1')
ys13_1 = Real('ys13_1')
ys14_1 = Real('ys14_1')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo1u = Real('xo1u')
xo1d = Real('xo1d')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=6, pi1>=5, pi2>=4, pi3>=3, pi4>=5, pi5>=4, pi6>=3, pi7>=2, pi8>=4, pi9>=3, pi10>=2, pi11>=1, pi12>=3, pi13>=2, pi14>=1, pi15>=0, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l) * (1 + pi0) + (ys0_1*xo1r) * (1 + pi1) + (ys0_1*xo1u) * (1 + pi0) + (ys0_1*xo1d) * (1 + pi4),
pi1 == (ys1_1*xo1l) * (1 + pi0) + (ys1_1*xo1r) * (1 + pi2) + (ys1_1*xo1u) * (1 + pi1) + (ys1_1*xo1d) * (1 + pi5),
pi2 == (ys2_1*xo1l) * (1 + pi1) + (ys2_1*xo1r) * (1 + pi3) + (ys2_1*xo1u) * (1 + pi2) + (ys2_1*xo1d) * (1 + pi6),
pi3 == (ys3_1*xo1l) * (1 + pi2) + (ys3_1*xo1r) * (1 + pi3) + (ys3_1*xo1u) * (1 + pi3) + (ys3_1*xo1d) * (1 + pi7),
pi4 == (ys4_1*xo1l) * (1 + pi4) + (ys4_1*xo1r) * (1 + pi5) + (ys4_1*xo1u) * (1 + pi0) + (ys4_1*xo1d) * (1 + pi8),
pi5 == (ys5_1*xo1l) * (1 + pi4) + (ys5_1*xo1r) * (1 + pi6) + (ys5_1*xo1u) * (1 + pi1) + (ys5_1*xo1d) * (1 + pi9),
pi6 == (ys6_1*xo1l) * (1 + pi5) + (ys6_1*xo1r) * (1 + pi7) + (ys6_1*xo1u) * (1 + pi2) + (ys6_1*xo1d) * (1 + pi10),
pi7 == (ys7_1*xo1l) * (1 + pi6) + (ys7_1*xo1r) * (1 + pi7) + (ys7_1*xo1u) * (1 + pi3) + (ys7_1*xo1d) * (1 + pi11),
pi8 == (ys8_1*xo1l) * (1 + pi8) + (ys8_1*xo1r) * (1 + pi9) + (ys8_1*xo1u) * (1 + pi4) + (ys8_1*xo1d) * (1 + pi12),
pi9 == (ys9_1*xo1l) * (1 + pi8) + (ys9_1*xo1r) * (1 + pi10) + (ys9_1*xo1u) * (1 + pi5) + (ys9_1*xo1d) * (1 + pi13),
pi10 == (ys10_1*xo1l) * (1 + pi9) + (ys10_1*xo1r) * (1 + pi11) + (ys10_1*xo1u) * (1 + pi6) + (ys10_1*xo1d) * (1 + pi14),
pi11 == (ys11_1*xo1l) * (1 + pi10) + (ys11_1*xo1r) * (1 + pi11) + (ys11_1*xo1u) * (1 + pi7) + (ys11_1*xo1d) * (1 + pi15),
pi12 == (ys12_1*xo1l) * (1 + pi12) + (ys12_1*xo1r) * (1 + pi13) + (ys12_1*xo1u) * (1 + pi8) + (ys12_1*xo1d) * (1 + pi12),
pi13 == (ys13_1*xo1l) * (1 + pi12) + (ys13_1*xo1r) * (1 + pi14) + (ys13_1*xo1u) * (1 + pi9) + (ys13_1*xo1d) * (1 + pi13),
pi14 == (ys14_1*xo1l) * (1 + pi13) + (ys14_1*xo1r) * (1 + pi15) + (ys14_1*xo1u) * (1 + pi10) + (ys14_1*xo1d) * (1 + pi14),
pi15 == 0, 
exp==((pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14)) * Q(1,15),
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
xo1u== 0.0,
xo1r== 0.5,
xo1d== 0.5,
xo1l== 0.0,
xo1u + xo1r + xo1d + xo1l == 1,
# Assigned observables
ys1_1 == 1,
ys6_1 == 1,
ys9_1 == 1,
ys0_1 == 1,
ys13_1 == 1,
ys5_1 == 1,
ys3_1 == 1,
ys8_1 == 1,
ys12_1 == 1,
ys11_1 == 1,
ys2_1 == 1,
ys10_1 == 1,
ys4_1 == 1,
ys14_1 == 1,
ys7_1 == 1,
# Every state should be mapped to exactly one equivalence class
ys0_1 == 1,
ys1_1 == 1,
ys2_1 == 1,
ys3_1 == 1,
ys4_1 == 1,
ys5_1 == 1,
ys6_1 == 1,
ys7_1 == 1,
ys8_1 == 1,
ys9_1 == 1,
ys10_1 == 1,
ys11_1 == 1,
ys12_1 == 1,
ys13_1 == 1,
ys14_1 == 1
)


sol = lambda : solver.model() if solver.check() == sat else "No Solution" if solver.check() == unsat else None
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
pi16 = Real('pi16')
pi17 = Real('pi17')
pi18 = Real('pi18')
pi19 = Real('pi19')
pi20 = Real('pi20')
pi21 = Real('pi21')
pi22 = Real('pi22')
pi23 = Real('pi23')
pi24 = Real('pi24')

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
ys15_1 = Real('ys15_1')
ys16_1 = Real('ys16_1')
ys17_1 = Real('ys17_1')
ys18_1 = Real('ys18_1')
ys19_1 = Real('ys19_1')
ys20_1 = Real('ys20_1')
ys21_1 = Real('ys21_1')
ys22_1 = Real('ys22_1')
ys23_1 = Real('ys23_1')
ys24_1 = Real('ys24_1')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo1u = Real('xo1u')
xo1d = Real('xo1d')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=5, pi1>=4, pi2>=4, pi3>=5, pi4>=6, pi5>=4, pi6>=3, pi7>=3, pi8>=4, pi9>=5, pi10>=3, pi11>=2, pi12>=2, pi13>=3, pi14>=4, pi15>=2, pi16>=1, pi17>=1, pi18>=2, pi19>=3, pi20>=1, pi21>=0, pi22>=0, pi23>=2, pi24>=3, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l) * (1 + pi0) + (ys0_1*xo1r) * (1 + pi1) + (ys0_1*xo1u) * (1 + pi0) + (ys0_1*xo1d) * (1 + pi5),
pi1 == (ys1_1*xo1l) * (1 + pi0) + (ys1_1*xo1r) * (1 + pi2) + (ys1_1*xo1u) * (1 + pi1) + (ys1_1*xo1d) * (1 + pi6),
pi2 == (ys2_1*xo1l) * (1 + pi1) + (ys2_1*xo1r) * (1 + pi3) + (ys2_1*xo1u) * (1 + pi2) + (ys2_1*xo1d) * (1 + pi7),
pi3 == (ys3_1*xo1l) * (1 + pi2) + (ys3_1*xo1r) * (1 + pi4) + (ys3_1*xo1u) * (1 + pi3) + (ys3_1*xo1d) * (1 + pi8),
pi4 == (ys4_1*xo1l) * (1 + pi3) + (ys4_1*xo1r) * (1 + pi4) + (ys4_1*xo1u) * (1 + pi4) + (ys4_1*xo1d) * (1 + pi9),
pi5 == (ys5_1*xo1l) * (1 + pi5) + (ys5_1*xo1r) * (1 + pi6) + (ys5_1*xo1u) * (1 + pi0) + (ys5_1*xo1d) * (1 + pi10),
pi6 == (ys6_1*xo1l) * (1 + pi5) + (ys6_1*xo1r) * (1 + pi7) + (ys6_1*xo1u) * (1 + pi1) + (ys6_1*xo1d) * (1 + pi11),
pi7 == (ys7_1*xo1l) * (1 + pi6) + (ys7_1*xo1r) * (1 + pi8) + (ys7_1*xo1u) * (1 + pi2) + (ys7_1*xo1d) * (1 + pi12),
pi8 == (ys8_1*xo1l) * (1 + pi7) + (ys8_1*xo1r) * (1 + pi9) + (ys8_1*xo1u) * (1 + pi3) + (ys8_1*xo1d) * (1 + pi13),
pi9 == (ys9_1*xo1l) * (1 + pi8) + (ys9_1*xo1r) * (1 + pi9) + (ys9_1*xo1u) * (1 + pi4) + (ys9_1*xo1d) * (1 + pi14),
pi10 == (ys10_1*xo1l) * (1 + pi10) + (ys10_1*xo1r) * (1 + pi11) + (ys10_1*xo1u) * (1 + pi5) + (ys10_1*xo1d) * (1 + pi15),
pi11 == (ys11_1*xo1l) * (1 + pi10) + (ys11_1*xo1r) * (1 + pi12) + (ys11_1*xo1u) * (1 + pi6) + (ys11_1*xo1d) * (1 + pi16),
pi12 == (ys12_1*xo1l) * (1 + pi11) + (ys12_1*xo1r) * (1 + pi13) + (ys12_1*xo1u) * (1 + pi7) + (ys12_1*xo1d) * (1 + pi17),
pi13 == (ys13_1*xo1l) * (1 + pi12) + (ys13_1*xo1r) * (1 + pi14) + (ys13_1*xo1u) * (1 + pi8) + (ys13_1*xo1d) * (1 + pi18),
pi14 == (ys14_1*xo1l) * (1 + pi13) + (ys14_1*xo1r) * (1 + pi14) + (ys14_1*xo1u) * (1 + pi9) + (ys14_1*xo1d) * (1 + pi19),
pi15 == (ys15_1*xo1l) * (1 + pi15) + (ys15_1*xo1r) * (1 + pi16) + (ys15_1*xo1u) * (1 + pi10) + (ys15_1*xo1d) * (1 + pi20),
pi16 == (ys16_1*xo1l) * (1 + pi15) + (ys16_1*xo1r) * (1 + pi17) + (ys16_1*xo1u) * (1 + pi11) + (ys16_1*xo1d) * (1 + pi21),
pi17 == (ys17_1*xo1l) * (1 + pi16) + (ys17_1*xo1r) * (1 + pi18) + (ys17_1*xo1u) * (1 + pi12) + (ys17_1*xo1d) * (1 + pi22),
pi18 == (ys18_1*xo1l) * (1 + pi17) + (ys18_1*xo1r) * (1 + pi19) + (ys18_1*xo1u) * (1 + pi13) + (ys18_1*xo1d) * (1 + pi23),
pi19 == (ys19_1*xo1l) * (1 + pi18) + (ys19_1*xo1r) * (1 + pi19) + (ys19_1*xo1u) * (1 + pi14) + (ys19_1*xo1d) * (1 + pi24),
pi20 == (ys20_1*xo1l) * (1 + pi20) + (ys20_1*xo1r) * (1 + pi21) + (ys20_1*xo1u) * (1 + pi15) + (ys20_1*xo1d) * (1 + pi20),
pi21 == 0, 
pi22 == (ys22_1*xo1l) * (1 + pi21) + (ys22_1*xo1r) * (1 + pi23) + (ys22_1*xo1u) * (1 + pi17) + (ys22_1*xo1d) * (1 + pi22),
pi23 == (ys23_1*xo1l) * (1 + pi22) + (ys23_1*xo1r) * (1 + pi24) + (ys23_1*xo1u) * (1 + pi18) + (ys23_1*xo1d) * (1 + pi23),
pi24 == (ys24_1*xo1l) * (1 + pi23) + (ys24_1*xo1r) * (1 + pi24) + (ys24_1*xo1u) * (1 + pi19) + (ys24_1*xo1d) * (1 + pi24),
exp==((pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi22+pi23+pi24)) * Q(1,24),
# Randomised strategies (proper probability distributions)
xo1l>= 0,
xo1l<= 1,
xo1r>= 0,
xo1r<= 1,
xo1u>= 0,
xo1u<= 1,
xo1d>= 0,
xo1d<= 1,
# Assigning the action probability distribution from the strategies
xo1u== Q(0, 1),
xo1r== Q(0, 1),
xo1d== Q(1, 1),
xo1l== Q(0, 1),
xo1u + xo1r + xo1d + xo1l == 1,
# Assigned observables
ys20_1 == 1,
ys19_1 == 1,
ys23_1 == 1,
ys16_1 == 1,
ys2_1 == 1,
ys12_1 == 1,
ys5_1 == 1,
ys8_1 == 1,
ys22_1 == 1,
ys15_1 == 1,
ys18_1 == 1,
ys1_1 == 1,
ys14_1 == 1,
ys7_1 == 1,
ys4_1 == 1,
ys11_1 == 1,
ys17_1 == 1,
ys24_1 == 1,
ys0_1 == 1,
ys6_1 == 1,
ys3_1 == 1,
ys10_1 == 1,
ys9_1 == 1,
ys13_1 == 1,
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
ys14_1 == 1,
ys15_1 == 1,
ys16_1 == 1,
ys17_1 == 1,
ys18_1 == 1,
ys19_1 == 1,
ys20_1 == 1,
ys22_1 == 1,
ys23_1 == 1,
ys24_1 == 1
)


sol = lambda : solver.model() if solver.check() == sat else "No Solution" if solver.check() == unsat else None
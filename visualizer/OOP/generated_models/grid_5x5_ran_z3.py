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
ys0_2 = Real('ys0_2')
ys1_1 = Real('ys1_1')
ys1_2 = Real('ys1_2')
ys2_1 = Real('ys2_1')
ys2_2 = Real('ys2_2')
ys3_1 = Real('ys3_1')
ys3_2 = Real('ys3_2')
ys4_1 = Real('ys4_1')
ys4_2 = Real('ys4_2')
ys5_1 = Real('ys5_1')
ys5_2 = Real('ys5_2')
ys6_1 = Real('ys6_1')
ys6_2 = Real('ys6_2')
ys7_1 = Real('ys7_1')
ys7_2 = Real('ys7_2')
ys8_1 = Real('ys8_1')
ys8_2 = Real('ys8_2')
ys9_1 = Real('ys9_1')
ys9_2 = Real('ys9_2')
ys10_1 = Real('ys10_1')
ys10_2 = Real('ys10_2')
ys11_1 = Real('ys11_1')
ys11_2 = Real('ys11_2')
ys12_1 = Real('ys12_1')
ys12_2 = Real('ys12_2')
ys13_1 = Real('ys13_1')
ys13_2 = Real('ys13_2')
ys14_1 = Real('ys14_1')
ys14_2 = Real('ys14_2')
ys15_1 = Real('ys15_1')
ys15_2 = Real('ys15_2')
ys16_1 = Real('ys16_1')
ys16_2 = Real('ys16_2')
ys17_1 = Real('ys17_1')
ys17_2 = Real('ys17_2')
ys18_1 = Real('ys18_1')
ys18_2 = Real('ys18_2')
ys19_1 = Real('ys19_1')
ys19_2 = Real('ys19_2')
ys20_1 = Real('ys20_1')
ys20_2 = Real('ys20_2')
ys22_1 = Real('ys22_1')
ys22_2 = Real('ys22_2')
ys23_1 = Real('ys23_1')
ys23_2 = Real('ys23_2')
ys24_1 = Real('ys24_1')
ys24_2 = Real('ys24_2')

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
pi0>=5, pi1>=4, pi2>=4, pi3>=5, pi4>=6, pi5>=4, pi6>=3, pi7>=3, pi8>=4, pi9>=5, pi10>=3, pi11>=2, pi12>=2, pi13>=3, pi14>=4, pi15>=2, pi16>=1, pi17>=1, pi18>=2, pi19>=3, pi20>=1, pi21>=0, pi22>=0, pi23>=2, pi24>=3, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l + ys0_2*xo2l) * (1 + pi0) + (ys0_1*xo1r + ys0_2*xo2r) * (1 + pi1) + (ys0_1*xo1u + ys0_2*xo2u) * (1 + pi0) + (ys0_1*xo1d + ys0_2*xo2d) * (1 + pi5),
pi1 == (ys1_1*xo1l + ys1_2*xo2l) * (1 + pi0) + (ys1_1*xo1r + ys1_2*xo2r) * (1 + pi2) + (ys1_1*xo1u + ys1_2*xo2u) * (1 + pi1) + (ys1_1*xo1d + ys1_2*xo2d) * (1 + pi6),
pi2 == (ys2_1*xo1l + ys2_2*xo2l) * (1 + pi1) + (ys2_1*xo1r + ys2_2*xo2r) * (1 + pi3) + (ys2_1*xo1u + ys2_2*xo2u) * (1 + pi2) + (ys2_1*xo1d + ys2_2*xo2d) * (1 + pi7),
pi3 == (ys3_1*xo1l + ys3_2*xo2l) * (1 + pi2) + (ys3_1*xo1r + ys3_2*xo2r) * (1 + pi4) + (ys3_1*xo1u + ys3_2*xo2u) * (1 + pi3) + (ys3_1*xo1d + ys3_2*xo2d) * (1 + pi8),
pi4 == (ys4_1*xo1l + ys4_2*xo2l) * (1 + pi3) + (ys4_1*xo1r + ys4_2*xo2r) * (1 + pi4) + (ys4_1*xo1u + ys4_2*xo2u) * (1 + pi4) + (ys4_1*xo1d + ys4_2*xo2d) * (1 + pi9),
pi5 == (ys5_1*xo1l + ys5_2*xo2l) * (1 + pi5) + (ys5_1*xo1r + ys5_2*xo2r) * (1 + pi6) + (ys5_1*xo1u + ys5_2*xo2u) * (1 + pi0) + (ys5_1*xo1d + ys5_2*xo2d) * (1 + pi10),
pi6 == (ys6_1*xo1l + ys6_2*xo2l) * (1 + pi5) + (ys6_1*xo1r + ys6_2*xo2r) * (1 + pi7) + (ys6_1*xo1u + ys6_2*xo2u) * (1 + pi1) + (ys6_1*xo1d + ys6_2*xo2d) * (1 + pi11),
pi7 == (ys7_1*xo1l + ys7_2*xo2l) * (1 + pi6) + (ys7_1*xo1r + ys7_2*xo2r) * (1 + pi8) + (ys7_1*xo1u + ys7_2*xo2u) * (1 + pi2) + (ys7_1*xo1d + ys7_2*xo2d) * (1 + pi12),
pi8 == (ys8_1*xo1l + ys8_2*xo2l) * (1 + pi7) + (ys8_1*xo1r + ys8_2*xo2r) * (1 + pi9) + (ys8_1*xo1u + ys8_2*xo2u) * (1 + pi3) + (ys8_1*xo1d + ys8_2*xo2d) * (1 + pi13),
pi9 == (ys9_1*xo1l + ys9_2*xo2l) * (1 + pi8) + (ys9_1*xo1r + ys9_2*xo2r) * (1 + pi9) + (ys9_1*xo1u + ys9_2*xo2u) * (1 + pi4) + (ys9_1*xo1d + ys9_2*xo2d) * (1 + pi14),
pi10 == (ys10_1*xo1l + ys10_2*xo2l) * (1 + pi10) + (ys10_1*xo1r + ys10_2*xo2r) * (1 + pi11) + (ys10_1*xo1u + ys10_2*xo2u) * (1 + pi5) + (ys10_1*xo1d + ys10_2*xo2d) * (1 + pi15),
pi11 == (ys11_1*xo1l + ys11_2*xo2l) * (1 + pi10) + (ys11_1*xo1r + ys11_2*xo2r) * (1 + pi12) + (ys11_1*xo1u + ys11_2*xo2u) * (1 + pi6) + (ys11_1*xo1d + ys11_2*xo2d) * (1 + pi16),
pi12 == (ys12_1*xo1l + ys12_2*xo2l) * (1 + pi11) + (ys12_1*xo1r + ys12_2*xo2r) * (1 + pi13) + (ys12_1*xo1u + ys12_2*xo2u) * (1 + pi7) + (ys12_1*xo1d + ys12_2*xo2d) * (1 + pi17),
pi13 == (ys13_1*xo1l + ys13_2*xo2l) * (1 + pi12) + (ys13_1*xo1r + ys13_2*xo2r) * (1 + pi14) + (ys13_1*xo1u + ys13_2*xo2u) * (1 + pi8) + (ys13_1*xo1d + ys13_2*xo2d) * (1 + pi18),
pi14 == (ys14_1*xo1l + ys14_2*xo2l) * (1 + pi13) + (ys14_1*xo1r + ys14_2*xo2r) * (1 + pi14) + (ys14_1*xo1u + ys14_2*xo2u) * (1 + pi9) + (ys14_1*xo1d + ys14_2*xo2d) * (1 + pi19),
pi15 == (ys15_1*xo1l + ys15_2*xo2l) * (1 + pi15) + (ys15_1*xo1r + ys15_2*xo2r) * (1 + pi16) + (ys15_1*xo1u + ys15_2*xo2u) * (1 + pi10) + (ys15_1*xo1d + ys15_2*xo2d) * (1 + pi20),
pi16 == (ys16_1*xo1l + ys16_2*xo2l) * (1 + pi15) + (ys16_1*xo1r + ys16_2*xo2r) * (1 + pi17) + (ys16_1*xo1u + ys16_2*xo2u) * (1 + pi11) + (ys16_1*xo1d + ys16_2*xo2d) * (1 + pi21),
pi17 == (ys17_1*xo1l + ys17_2*xo2l) * (1 + pi16) + (ys17_1*xo1r + ys17_2*xo2r) * (1 + pi18) + (ys17_1*xo1u + ys17_2*xo2u) * (1 + pi12) + (ys17_1*xo1d + ys17_2*xo2d) * (1 + pi22),
pi18 == (ys18_1*xo1l + ys18_2*xo2l) * (1 + pi17) + (ys18_1*xo1r + ys18_2*xo2r) * (1 + pi19) + (ys18_1*xo1u + ys18_2*xo2u) * (1 + pi13) + (ys18_1*xo1d + ys18_2*xo2d) * (1 + pi23),
pi19 == (ys19_1*xo1l + ys19_2*xo2l) * (1 + pi18) + (ys19_1*xo1r + ys19_2*xo2r) * (1 + pi19) + (ys19_1*xo1u + ys19_2*xo2u) * (1 + pi14) + (ys19_1*xo1d + ys19_2*xo2d) * (1 + pi24),
pi20 == (ys20_1*xo1l + ys20_2*xo2l) * (1 + pi20) + (ys20_1*xo1r + ys20_2*xo2r) * (1 + pi21) + (ys20_1*xo1u + ys20_2*xo2u) * (1 + pi15) + (ys20_1*xo1d + ys20_2*xo2d) * (1 + pi20),
pi21 == 0, 
pi22 == (ys22_1*xo1l + ys22_2*xo2l) * (1 + pi21) + (ys22_1*xo1r + ys22_2*xo2r) * (1 + pi23) + (ys22_1*xo1u + ys22_2*xo2u) * (1 + pi17) + (ys22_1*xo1d + ys22_2*xo2d) * (1 + pi22),
pi23 == (ys23_1*xo1l + ys23_2*xo2l) * (1 + pi22) + (ys23_1*xo1r + ys23_2*xo2r) * (1 + pi24) + (ys23_1*xo1u + ys23_2*xo2u) * (1 + pi18) + (ys23_1*xo1d + ys23_2*xo2d) * (1 + pi23),
pi24 == (ys24_1*xo1l + ys24_2*xo2l) * (1 + pi23) + (ys24_1*xo1r + ys24_2*xo2r) * (1 + pi24) + (ys24_1*xo1u + ys24_2*xo2u) * (1 + pi19) + (ys24_1*xo1d + ys24_2*xo2d) * (1 + pi24),
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= 5
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi22+pi23+pi24) * Q(1,24) <= 5,
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
# ysNM is a function that should map every state N to some observable class M
Or(ys0_1== 0 , ys0_1== 1),
Or(ys0_2== 0 , ys0_2== 1),
Or(ys1_1== 0 , ys1_1== 1),
Or(ys1_2== 0 , ys1_2== 1),
Or(ys2_1== 0 , ys2_1== 1),
Or(ys2_2== 0 , ys2_2== 1),
Or(ys3_1== 0 , ys3_1== 1),
Or(ys3_2== 0 , ys3_2== 1),
Or(ys4_1== 0 , ys4_1== 1),
Or(ys4_2== 0 , ys4_2== 1),
Or(ys5_1== 0 , ys5_1== 1),
Or(ys5_2== 0 , ys5_2== 1),
Or(ys6_1== 0 , ys6_1== 1),
Or(ys6_2== 0 , ys6_2== 1),
Or(ys7_1== 0 , ys7_1== 1),
Or(ys7_2== 0 , ys7_2== 1),
Or(ys8_1== 0 , ys8_1== 1),
Or(ys8_2== 0 , ys8_2== 1),
Or(ys9_1== 0 , ys9_1== 1),
Or(ys9_2== 0 , ys9_2== 1),
Or(ys10_1== 0 , ys10_1== 1),
Or(ys10_2== 0 , ys10_2== 1),
Or(ys11_1== 0 , ys11_1== 1),
Or(ys11_2== 0 , ys11_2== 1),
Or(ys12_1== 0 , ys12_1== 1),
Or(ys12_2== 0 , ys12_2== 1),
Or(ys13_1== 0 , ys13_1== 1),
Or(ys13_2== 0 , ys13_2== 1),
Or(ys14_1== 0 , ys14_1== 1),
Or(ys14_2== 0 , ys14_2== 1),
Or(ys15_1== 0 , ys15_1== 1),
Or(ys15_2== 0 , ys15_2== 1),
Or(ys16_1== 0 , ys16_1== 1),
Or(ys16_2== 0 , ys16_2== 1),
Or(ys17_1== 0 , ys17_1== 1),
Or(ys17_2== 0 , ys17_2== 1),
Or(ys18_1== 0 , ys18_1== 1),
Or(ys18_2== 0 , ys18_2== 1),
Or(ys19_1== 0 , ys19_1== 1),
Or(ys19_2== 0 , ys19_2== 1),
Or(ys20_1== 0 , ys20_1== 1),
Or(ys20_2== 0 , ys20_2== 1),
Or(ys22_1== 0 , ys22_1== 1),
Or(ys22_2== 0 , ys22_2== 1),
Or(ys23_1== 0 , ys23_1== 1),
Or(ys23_2== 0 , ys23_2== 1),
Or(ys24_1== 0 , ys24_1== 1),
Or(ys24_2== 0 , ys24_2== 1),
# Every state should be mapped to exactly one equivalence class
ys0_1 + ys0_2 == 1,
ys1_1 + ys1_2 == 1,
ys2_1 + ys2_2 == 1,
ys3_1 + ys3_2 == 1,
ys4_1 + ys4_2 == 1,
ys5_1 + ys5_2 == 1,
ys6_1 + ys6_2 == 1,
ys7_1 + ys7_2 == 1,
ys8_1 + ys8_2 == 1,
ys9_1 + ys9_2 == 1,
ys10_1 + ys10_2 == 1,
ys11_1 + ys11_2 == 1,
ys12_1 + ys12_2 == 1,
ys13_1 + ys13_2 == 1,
ys14_1 + ys14_2 == 1,
ys15_1 + ys15_2 == 1,
ys16_1 + ys16_2 == 1,
ys17_1 + ys17_2 == 1,
ys18_1 + ys18_2 == 1,
ys19_1 + ys19_2 == 1,
ys20_1 + ys20_2 == 1,
ys22_1 + ys22_2 == 1,
ys23_1 + ys23_2 == 1,
ys24_1 + ys24_2 == 1
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
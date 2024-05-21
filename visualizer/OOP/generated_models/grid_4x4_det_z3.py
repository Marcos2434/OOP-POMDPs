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

# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)
ys0_1 = Real('ys0_1')
ys0_2 = Real('ys0_2')
ys0_3 = Real('ys0_3')
ys1_1 = Real('ys1_1')
ys1_2 = Real('ys1_2')
ys1_3 = Real('ys1_3')
ys2_1 = Real('ys2_1')
ys2_2 = Real('ys2_2')
ys2_3 = Real('ys2_3')
ys3_1 = Real('ys3_1')
ys3_2 = Real('ys3_2')
ys3_3 = Real('ys3_3')
ys4_1 = Real('ys4_1')
ys4_2 = Real('ys4_2')
ys4_3 = Real('ys4_3')
ys5_1 = Real('ys5_1')
ys5_2 = Real('ys5_2')
ys5_3 = Real('ys5_3')
ys6_1 = Real('ys6_1')
ys6_2 = Real('ys6_2')
ys6_3 = Real('ys6_3')
ys7_1 = Real('ys7_1')
ys7_2 = Real('ys7_2')
ys7_3 = Real('ys7_3')
ys8_1 = Real('ys8_1')
ys8_2 = Real('ys8_2')
ys8_3 = Real('ys8_3')
ys9_1 = Real('ys9_1')
ys9_2 = Real('ys9_2')
ys9_3 = Real('ys9_3')
ys10_1 = Real('ys10_1')
ys10_2 = Real('ys10_2')
ys10_3 = Real('ys10_3')
ys11_1 = Real('ys11_1')
ys11_2 = Real('ys11_2')
ys11_3 = Real('ys11_3')
ys12_1 = Real('ys12_1')
ys12_2 = Real('ys12_2')
ys12_3 = Real('ys12_3')
ys14_1 = Real('ys14_1')
ys14_2 = Real('ys14_2')
ys14_3 = Real('ys14_3')
ys15_1 = Real('ys15_1')
ys15_2 = Real('ys15_2')
ys15_3 = Real('ys15_3')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo1u = Real('xo1u')
xo1d = Real('xo1d')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
xo2u = Real('xo2u')
xo2d = Real('xo2d')
xo3l = Real('xo3l')
xo3r = Real('xo3r')
xo3u = Real('xo3u')
xo3d = Real('xo3d')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=4, pi1>=3, pi2>=3, pi3>=4, pi4>=3, pi5>=2, pi6>=2, pi7>=3, pi8>=2, pi9>=1, pi10>=1, pi11>=2, pi12>=1, pi13>=0, pi14>=0, pi15>=2, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l + ys0_2*xo2l + ys0_3*xo3l) * (1 + pi0) + (ys0_1*xo1r + ys0_2*xo2r + ys0_3*xo3r) * (1 + pi1) + (ys0_1*xo1u + ys0_2*xo2u + ys0_3*xo3u) * (1 + pi0) + (ys0_1*xo1d + ys0_2*xo2d + ys0_3*xo3d) * (1 + pi4),
pi1 == (ys1_1*xo1l + ys1_2*xo2l + ys1_3*xo3l) * (1 + pi0) + (ys1_1*xo1r + ys1_2*xo2r + ys1_3*xo3r) * (1 + pi2) + (ys1_1*xo1u + ys1_2*xo2u + ys1_3*xo3u) * (1 + pi1) + (ys1_1*xo1d + ys1_2*xo2d + ys1_3*xo3d) * (1 + pi5),
pi2 == (ys2_1*xo1l + ys2_2*xo2l + ys2_3*xo3l) * (1 + pi1) + (ys2_1*xo1r + ys2_2*xo2r + ys2_3*xo3r) * (1 + pi3) + (ys2_1*xo1u + ys2_2*xo2u + ys2_3*xo3u) * (1 + pi2) + (ys2_1*xo1d + ys2_2*xo2d + ys2_3*xo3d) * (1 + pi6),
pi3 == (ys3_1*xo1l + ys3_2*xo2l + ys3_3*xo3l) * (1 + pi2) + (ys3_1*xo1r + ys3_2*xo2r + ys3_3*xo3r) * (1 + pi3) + (ys3_1*xo1u + ys3_2*xo2u + ys3_3*xo3u) * (1 + pi3) + (ys3_1*xo1d + ys3_2*xo2d + ys3_3*xo3d) * (1 + pi7),
pi4 == (ys4_1*xo1l + ys4_2*xo2l + ys4_3*xo3l) * (1 + pi4) + (ys4_1*xo1r + ys4_2*xo2r + ys4_3*xo3r) * (1 + pi5) + (ys4_1*xo1u + ys4_2*xo2u + ys4_3*xo3u) * (1 + pi0) + (ys4_1*xo1d + ys4_2*xo2d + ys4_3*xo3d) * (1 + pi8),
pi5 == (ys5_1*xo1l + ys5_2*xo2l + ys5_3*xo3l) * (1 + pi4) + (ys5_1*xo1r + ys5_2*xo2r + ys5_3*xo3r) * (1 + pi6) + (ys5_1*xo1u + ys5_2*xo2u + ys5_3*xo3u) * (1 + pi1) + (ys5_1*xo1d + ys5_2*xo2d + ys5_3*xo3d) * (1 + pi9),
pi6 == (ys6_1*xo1l + ys6_2*xo2l + ys6_3*xo3l) * (1 + pi5) + (ys6_1*xo1r + ys6_2*xo2r + ys6_3*xo3r) * (1 + pi7) + (ys6_1*xo1u + ys6_2*xo2u + ys6_3*xo3u) * (1 + pi2) + (ys6_1*xo1d + ys6_2*xo2d + ys6_3*xo3d) * (1 + pi10),
pi7 == (ys7_1*xo1l + ys7_2*xo2l + ys7_3*xo3l) * (1 + pi6) + (ys7_1*xo1r + ys7_2*xo2r + ys7_3*xo3r) * (1 + pi7) + (ys7_1*xo1u + ys7_2*xo2u + ys7_3*xo3u) * (1 + pi3) + (ys7_1*xo1d + ys7_2*xo2d + ys7_3*xo3d) * (1 + pi11),
pi8 == (ys8_1*xo1l + ys8_2*xo2l + ys8_3*xo3l) * (1 + pi8) + (ys8_1*xo1r + ys8_2*xo2r + ys8_3*xo3r) * (1 + pi9) + (ys8_1*xo1u + ys8_2*xo2u + ys8_3*xo3u) * (1 + pi4) + (ys8_1*xo1d + ys8_2*xo2d + ys8_3*xo3d) * (1 + pi12),
pi9 == (ys9_1*xo1l + ys9_2*xo2l + ys9_3*xo3l) * (1 + pi8) + (ys9_1*xo1r + ys9_2*xo2r + ys9_3*xo3r) * (1 + pi10) + (ys9_1*xo1u + ys9_2*xo2u + ys9_3*xo3u) * (1 + pi5) + (ys9_1*xo1d + ys9_2*xo2d + ys9_3*xo3d) * (1 + pi13),
pi10 == (ys10_1*xo1l + ys10_2*xo2l + ys10_3*xo3l) * (1 + pi9) + (ys10_1*xo1r + ys10_2*xo2r + ys10_3*xo3r) * (1 + pi11) + (ys10_1*xo1u + ys10_2*xo2u + ys10_3*xo3u) * (1 + pi6) + (ys10_1*xo1d + ys10_2*xo2d + ys10_3*xo3d) * (1 + pi14),
pi11 == (ys11_1*xo1l + ys11_2*xo2l + ys11_3*xo3l) * (1 + pi10) + (ys11_1*xo1r + ys11_2*xo2r + ys11_3*xo3r) * (1 + pi11) + (ys11_1*xo1u + ys11_2*xo2u + ys11_3*xo3u) * (1 + pi7) + (ys11_1*xo1d + ys11_2*xo2d + ys11_3*xo3d) * (1 + pi15),
pi12 == (ys12_1*xo1l + ys12_2*xo2l + ys12_3*xo3l) * (1 + pi12) + (ys12_1*xo1r + ys12_2*xo2r + ys12_3*xo3r) * (1 + pi13) + (ys12_1*xo1u + ys12_2*xo2u + ys12_3*xo3u) * (1 + pi8) + (ys12_1*xo1d + ys12_2*xo2d + ys12_3*xo3d) * (1 + pi12),
pi13 == 0, 
pi14 == (ys14_1*xo1l + ys14_2*xo2l + ys14_3*xo3l) * (1 + pi13) + (ys14_1*xo1r + ys14_2*xo2r + ys14_3*xo3r) * (1 + pi15) + (ys14_1*xo1u + ys14_2*xo2u + ys14_3*xo3u) * (1 + pi10) + (ys14_1*xo1d + ys14_2*xo2d + ys14_3*xo3d) * (1 + pi14),
pi15 == (ys15_1*xo1l + ys15_2*xo2l + ys15_3*xo3l) * (1 + pi14) + (ys15_1*xo1r + ys15_2*xo2r + ys15_3*xo3r) * (1 + pi15) + (ys15_1*xo1u + ys15_2*xo2u + ys15_3*xo3u) * (1 + pi11) + (ys15_1*xo1d + ys15_2*xo2d + ys15_3*xo3d) * (1 + pi15),
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= 3.3
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi14+pi15) * Q(1,15) <= 3.3,
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
xo3l>= 0,
xo3l<= 1,
xo3r>= 0,
xo3r<= 1,
xo3u>= 0,
xo3u<= 1,
xo3d>= 0,
xo3d<= 1,
xo1l + xo1r + xo1u + xo1d == 1,
xo2l + xo2r + xo2u + xo2d == 1,
xo3l + xo3r + xo3u + xo3d == 1,
# Deterministic Strategies activated
Or(xo1l == 0, xo1l == 1),
Or(xo1r == 0, xo1r == 1),
Or(xo1u == 0, xo1u == 1),
Or(xo1d == 0, xo1d == 1),
Or(xo2l == 0, xo2l == 1),
Or(xo2r == 0, xo2r == 1),
Or(xo2u == 0, xo2u == 1),
Or(xo2d == 0, xo2d == 1),
Or(xo3l == 0, xo3l == 1),
Or(xo3r == 0, xo3r == 1),
Or(xo3u == 0, xo3u == 1),
Or(xo3d == 0, xo3d == 1),
# ysNM is a function that should map every state N to some observable class M
Or(ys0_1== 0 , ys0_1== 1),
Or(ys0_2== 0 , ys0_2== 1),
Or(ys0_3== 0 , ys0_3== 1),
Or(ys1_1== 0 , ys1_1== 1),
Or(ys1_2== 0 , ys1_2== 1),
Or(ys1_3== 0 , ys1_3== 1),
Or(ys2_1== 0 , ys2_1== 1),
Or(ys2_2== 0 , ys2_2== 1),
Or(ys2_3== 0 , ys2_3== 1),
Or(ys3_1== 0 , ys3_1== 1),
Or(ys3_2== 0 , ys3_2== 1),
Or(ys3_3== 0 , ys3_3== 1),
Or(ys4_1== 0 , ys4_1== 1),
Or(ys4_2== 0 , ys4_2== 1),
Or(ys4_3== 0 , ys4_3== 1),
Or(ys5_1== 0 , ys5_1== 1),
Or(ys5_2== 0 , ys5_2== 1),
Or(ys5_3== 0 , ys5_3== 1),
Or(ys6_1== 0 , ys6_1== 1),
Or(ys6_2== 0 , ys6_2== 1),
Or(ys6_3== 0 , ys6_3== 1),
Or(ys7_1== 0 , ys7_1== 1),
Or(ys7_2== 0 , ys7_2== 1),
Or(ys7_3== 0 , ys7_3== 1),
Or(ys8_1== 0 , ys8_1== 1),
Or(ys8_2== 0 , ys8_2== 1),
Or(ys8_3== 0 , ys8_3== 1),
Or(ys9_1== 0 , ys9_1== 1),
Or(ys9_2== 0 , ys9_2== 1),
Or(ys9_3== 0 , ys9_3== 1),
Or(ys10_1== 0 , ys10_1== 1),
Or(ys10_2== 0 , ys10_2== 1),
Or(ys10_3== 0 , ys10_3== 1),
Or(ys11_1== 0 , ys11_1== 1),
Or(ys11_2== 0 , ys11_2== 1),
Or(ys11_3== 0 , ys11_3== 1),
Or(ys12_1== 0 , ys12_1== 1),
Or(ys12_2== 0 , ys12_2== 1),
Or(ys12_3== 0 , ys12_3== 1),
Or(ys14_1== 0 , ys14_1== 1),
Or(ys14_2== 0 , ys14_2== 1),
Or(ys14_3== 0 , ys14_3== 1),
Or(ys15_1== 0 , ys15_1== 1),
Or(ys15_2== 0 , ys15_2== 1),
Or(ys15_3== 0 , ys15_3== 1),
# Every state should be mapped to exactly one equivalence class
ys0_1 + ys0_2 + ys0_3 == 1,
ys1_1 + ys1_2 + ys1_3 == 1,
ys2_1 + ys2_2 + ys2_3 == 1,
ys3_1 + ys3_2 + ys3_3 == 1,
ys4_1 + ys4_2 + ys4_3 == 1,
ys5_1 + ys5_2 + ys5_3 == 1,
ys6_1 + ys6_2 + ys6_3 == 1,
ys7_1 + ys7_2 + ys7_3 == 1,
ys8_1 + ys8_2 + ys8_3 == 1,
ys9_1 + ys9_2 + ys9_3 == 1,
ys10_1 + ys10_2 + ys10_3 == 1,
ys11_1 + ys11_2 + ys11_3 == 1,
ys12_1 + ys12_2 + ys12_3 == 1,
ys14_1 + ys14_2 + ys14_3 == 1,
ys15_1 + ys15_2 + ys15_3 == 1
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
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

# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)
ys0_1 = Real('ys0_1')
ys0_2 = Real('ys0_2')
ys0_3 = Real('ys0_3')
ys0_4 = Real('ys0_4')
ys1_1 = Real('ys1_1')
ys1_2 = Real('ys1_2')
ys1_3 = Real('ys1_3')
ys1_4 = Real('ys1_4')
ys2_1 = Real('ys2_1')
ys2_2 = Real('ys2_2')
ys2_3 = Real('ys2_3')
ys2_4 = Real('ys2_4')
ys3_1 = Real('ys3_1')
ys3_2 = Real('ys3_2')
ys3_3 = Real('ys3_3')
ys3_4 = Real('ys3_4')
ys4_1 = Real('ys4_1')
ys4_2 = Real('ys4_2')
ys4_3 = Real('ys4_3')
ys4_4 = Real('ys4_4')
ys5_1 = Real('ys5_1')
ys5_2 = Real('ys5_2')
ys5_3 = Real('ys5_3')
ys5_4 = Real('ys5_4')
ys6_1 = Real('ys6_1')
ys6_2 = Real('ys6_2')
ys6_3 = Real('ys6_3')
ys6_4 = Real('ys6_4')
ys7_1 = Real('ys7_1')
ys7_2 = Real('ys7_2')
ys7_3 = Real('ys7_3')
ys7_4 = Real('ys7_4')
ys8_1 = Real('ys8_1')
ys8_2 = Real('ys8_2')
ys8_3 = Real('ys8_3')
ys8_4 = Real('ys8_4')
ys10_1 = Real('ys10_1')
ys10_2 = Real('ys10_2')
ys10_3 = Real('ys10_3')
ys10_4 = Real('ys10_4')

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
xo4l = Real('xo4l')
xo4r = Real('xo4r')
xo4u = Real('xo4u')
xo4d = Real('xo4d')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=4, pi1>=3, pi2>=2, pi3>=3, pi4>=4, pi5>=5, pi6>=1, pi7>=5, pi8>=6, pi9>=0, pi10>=6, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l + ys0_2*xo2l + ys0_3*xo3l + ys0_4*xo4l) * (1 + pi0) + (ys0_1*xo1r + ys0_2*xo2r + ys0_3*xo3r + ys0_4*xo4r) * (1 + pi1) + (ys0_1*xo1u + ys0_2*xo2u + ys0_3*xo3u + ys0_4*xo4u) * (1 + pi0) + (ys0_1*xo1d + ys0_2*xo2d + ys0_3*xo3d + ys0_4*xo4d) * (1 + pi5),
pi1 == (ys1_1*xo1l + ys1_2*xo2l + ys1_3*xo3l + ys1_4*xo4l) * (1 + pi0) + (ys1_1*xo1r + ys1_2*xo2r + ys1_3*xo3r + ys1_4*xo4r) * (1 + pi2) + (ys1_1*xo1u + ys1_2*xo2u + ys1_3*xo3u + ys1_4*xo4u) * (1 + pi1) + (ys1_1*xo1d + ys1_2*xo2d + ys1_3*xo3d + ys1_4*xo4d) * (1 + pi1),
pi2 == (ys2_1*xo1l + ys2_2*xo2l + ys2_3*xo3l + ys2_4*xo4l) * (1 + pi1) + (ys2_1*xo1r + ys2_2*xo2r + ys2_3*xo3r + ys2_4*xo4r) * (1 + pi3) + (ys2_1*xo1u + ys2_2*xo2u + ys2_3*xo3u + ys2_4*xo4u) * (1 + pi2) + (ys2_1*xo1d + ys2_2*xo2d + ys2_3*xo3d + ys2_4*xo4d) * (1 + pi6),
pi3 == (ys3_1*xo1l + ys3_2*xo2l + ys3_3*xo3l + ys3_4*xo4l) * (1 + pi2) + (ys3_1*xo1r + ys3_2*xo2r + ys3_3*xo3r + ys3_4*xo4r) * (1 + pi4) + (ys3_1*xo1u + ys3_2*xo2u + ys3_3*xo3u + ys3_4*xo4u) * (1 + pi3) + (ys3_1*xo1d + ys3_2*xo2d + ys3_3*xo3d + ys3_4*xo4d) * (1 + pi3),
pi4 == (ys4_1*xo1l + ys4_2*xo2l + ys4_3*xo3l + ys4_4*xo4l) * (1 + pi3) + (ys4_1*xo1r + ys4_2*xo2r + ys4_3*xo3r + ys4_4*xo4r) * (1 + pi4) + (ys4_1*xo1u + ys4_2*xo2u + ys4_3*xo3u + ys4_4*xo4u) * (1 + pi4) + (ys4_1*xo1d + ys4_2*xo2d + ys4_3*xo3d + ys4_4*xo4d) * (1 + pi7),
pi5 == (ys5_1*xo1l + ys5_2*xo2l + ys5_3*xo3l + ys5_4*xo4l) * (1 + pi5) + (ys5_1*xo1r + ys5_2*xo2r + ys5_3*xo3r + ys5_4*xo4r) * (1 + pi5) + (ys5_1*xo1u + ys5_2*xo2u + ys5_3*xo3u + ys5_4*xo4u) * (1 + pi0) + (ys5_1*xo1d + ys5_2*xo2d + ys5_3*xo3d + ys5_4*xo4d) * (1 + pi8),
pi6 == (ys6_1*xo1l + ys6_2*xo2l + ys6_3*xo3l + ys6_4*xo4l) * (1 + pi6) + (ys6_1*xo1r + ys6_2*xo2r + ys6_3*xo3r + ys6_4*xo4r) * (1 + pi6) + (ys6_1*xo1u + ys6_2*xo2u + ys6_3*xo3u + ys6_4*xo4u) * (1 + pi2) + (ys6_1*xo1d + ys6_2*xo2d + ys6_3*xo3d + ys6_4*xo4d) * (1 + pi9),
pi7 == (ys7_1*xo1l + ys7_2*xo2l + ys7_3*xo3l + ys7_4*xo4l) * (1 + pi7) + (ys7_1*xo1r + ys7_2*xo2r + ys7_3*xo3r + ys7_4*xo4r) * (1 + pi7) + (ys7_1*xo1u + ys7_2*xo2u + ys7_3*xo3u + ys7_4*xo4u) * (1 + pi4) + (ys7_1*xo1d + ys7_2*xo2d + ys7_3*xo3d + ys7_4*xo4d) * (1 + pi10),
pi8 == (ys8_1*xo1l + ys8_2*xo2l + ys8_3*xo3l + ys8_4*xo4l) * (1 + pi8) + (ys8_1*xo1r + ys8_2*xo2r + ys8_3*xo3r + ys8_4*xo4r) * (1 + pi8) + (ys8_1*xo1u + ys8_2*xo2u + ys8_3*xo3u + ys8_4*xo4u) * (1 + pi5) + (ys8_1*xo1d + ys8_2*xo2d + ys8_3*xo3d + ys8_4*xo4d) * (1 + pi8),
pi9 == 0, 
pi10 == (ys10_1*xo1l + ys10_2*xo2l + ys10_3*xo3l + ys10_4*xo4l) * (1 + pi10) + (ys10_1*xo1r + ys10_2*xo2r + ys10_3*xo3r + ys10_4*xo4r) * (1 + pi10) + (ys10_1*xo1u + ys10_2*xo2u + ys10_3*xo3u + ys10_4*xo4u) * (1 + pi7) + (ys10_1*xo1d + ys10_2*xo2d + ys10_3*xo3d + ys10_4*xo4d) * (1 + pi10),
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= 3.9
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi10) * Q(1,10) <= 3.9,
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
xo4l>= 0,
xo4l<= 1,
xo4r>= 0,
xo4r<= 1,
xo4u>= 0,
xo4u<= 1,
xo4d>= 0,
xo4d<= 1,
xo1l + xo1r + xo1u + xo1d == 1,
xo2l + xo2r + xo2u + xo2d == 1,
xo3l + xo3r + xo3u + xo3d == 1,
xo4l + xo4r + xo4u + xo4d == 1,
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
Or(xo4l == 0, xo4l == 1),
Or(xo4r == 0, xo4r == 1),
Or(xo4u == 0, xo4u == 1),
Or(xo4d == 0, xo4d == 1),
# ysNM is a function that should map every state N to some observable class M
Or(ys0_1== 0 , ys0_1== 1),
Or(ys0_2== 0 , ys0_2== 1),
Or(ys0_3== 0 , ys0_3== 1),
Or(ys0_4== 0 , ys0_4== 1),
Or(ys1_1== 0 , ys1_1== 1),
Or(ys1_2== 0 , ys1_2== 1),
Or(ys1_3== 0 , ys1_3== 1),
Or(ys1_4== 0 , ys1_4== 1),
Or(ys2_1== 0 , ys2_1== 1),
Or(ys2_2== 0 , ys2_2== 1),
Or(ys2_3== 0 , ys2_3== 1),
Or(ys2_4== 0 , ys2_4== 1),
Or(ys3_1== 0 , ys3_1== 1),
Or(ys3_2== 0 , ys3_2== 1),
Or(ys3_3== 0 , ys3_3== 1),
Or(ys3_4== 0 , ys3_4== 1),
Or(ys4_1== 0 , ys4_1== 1),
Or(ys4_2== 0 , ys4_2== 1),
Or(ys4_3== 0 , ys4_3== 1),
Or(ys4_4== 0 , ys4_4== 1),
Or(ys5_1== 0 , ys5_1== 1),
Or(ys5_2== 0 , ys5_2== 1),
Or(ys5_3== 0 , ys5_3== 1),
Or(ys5_4== 0 , ys5_4== 1),
Or(ys6_1== 0 , ys6_1== 1),
Or(ys6_2== 0 , ys6_2== 1),
Or(ys6_3== 0 , ys6_3== 1),
Or(ys6_4== 0 , ys6_4== 1),
Or(ys7_1== 0 , ys7_1== 1),
Or(ys7_2== 0 , ys7_2== 1),
Or(ys7_3== 0 , ys7_3== 1),
Or(ys7_4== 0 , ys7_4== 1),
Or(ys8_1== 0 , ys8_1== 1),
Or(ys8_2== 0 , ys8_2== 1),
Or(ys8_3== 0 , ys8_3== 1),
Or(ys8_4== 0 , ys8_4== 1),
Or(ys10_1== 0 , ys10_1== 1),
Or(ys10_2== 0 , ys10_2== 1),
Or(ys10_3== 0 , ys10_3== 1),
Or(ys10_4== 0 , ys10_4== 1),
# Every state should be mapped to exactly one equivalence class
ys0_1 + ys0_2 + ys0_3 + ys0_4 == 1,
ys1_1 + ys1_2 + ys1_3 + ys1_4 == 1,
ys2_1 + ys2_2 + ys2_3 + ys2_4 == 1,
ys3_1 + ys3_2 + ys3_3 + ys3_4 == 1,
ys4_1 + ys4_2 + ys4_3 + ys4_4 == 1,
ys5_1 + ys5_2 + ys5_3 + ys5_4 == 1,
ys6_1 + ys6_2 + ys6_3 + ys6_4 == 1,
ys7_1 + ys7_2 + ys7_3 + ys7_4 == 1,
ys8_1 + ys8_2 + ys8_3 + ys8_4 == 1,
ys10_1 + ys10_2 + ys10_3 + ys10_4 == 1
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
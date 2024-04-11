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
ys0_2 = Real('ys0_2')
ys0_3 = Real('ys0_3')
ys0_4 = Real('ys0_4')
ys0_5 = Real('ys0_5')
ys0_6 = Real('ys0_6')
ys0_7 = Real('ys0_7')
ys0_8 = Real('ys0_8')
ys1_1 = Real('ys1_1')
ys1_2 = Real('ys1_2')
ys1_3 = Real('ys1_3')
ys1_4 = Real('ys1_4')
ys1_5 = Real('ys1_5')
ys1_6 = Real('ys1_6')
ys1_7 = Real('ys1_7')
ys1_8 = Real('ys1_8')
ys2_1 = Real('ys2_1')
ys2_2 = Real('ys2_2')
ys2_3 = Real('ys2_3')
ys2_4 = Real('ys2_4')
ys2_5 = Real('ys2_5')
ys2_6 = Real('ys2_6')
ys2_7 = Real('ys2_7')
ys2_8 = Real('ys2_8')
ys3_1 = Real('ys3_1')
ys3_2 = Real('ys3_2')
ys3_3 = Real('ys3_3')
ys3_4 = Real('ys3_4')
ys3_5 = Real('ys3_5')
ys3_6 = Real('ys3_6')
ys3_7 = Real('ys3_7')
ys3_8 = Real('ys3_8')
ys4_1 = Real('ys4_1')
ys4_2 = Real('ys4_2')
ys4_3 = Real('ys4_3')
ys4_4 = Real('ys4_4')
ys4_5 = Real('ys4_5')
ys4_6 = Real('ys4_6')
ys4_7 = Real('ys4_7')
ys4_8 = Real('ys4_8')
ys5_1 = Real('ys5_1')
ys5_2 = Real('ys5_2')
ys5_3 = Real('ys5_3')
ys5_4 = Real('ys5_4')
ys5_5 = Real('ys5_5')
ys5_6 = Real('ys5_6')
ys5_7 = Real('ys5_7')
ys5_8 = Real('ys5_8')
ys6_1 = Real('ys6_1')
ys6_2 = Real('ys6_2')
ys6_3 = Real('ys6_3')
ys6_4 = Real('ys6_4')
ys6_5 = Real('ys6_5')
ys6_6 = Real('ys6_6')
ys6_7 = Real('ys6_7')
ys6_8 = Real('ys6_8')
ys7_1 = Real('ys7_1')
ys7_2 = Real('ys7_2')
ys7_3 = Real('ys7_3')
ys7_4 = Real('ys7_4')
ys7_5 = Real('ys7_5')
ys7_6 = Real('ys7_6')
ys7_7 = Real('ys7_7')
ys7_8 = Real('ys7_8')

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
xo5l = Real('xo5l')
xo5r = Real('xo5r')
xo5u = Real('xo5u')
xo5d = Real('xo5d')
xo6l = Real('xo6l')
xo6r = Real('xo6r')
xo6u = Real('xo6u')
xo6d = Real('xo6d')
xo7l = Real('xo7l')
xo7r = Real('xo7r')
xo7u = Real('xo7u')
xo7d = Real('xo7d')
xo8l = Real('xo8l')
xo8r = Real('xo8r')
xo8u = Real('xo8u')
xo8d = Real('xo8d')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=4, pi1>=3, pi2>=2, pi3>=3, pi4>=2, pi5>=1, pi6>=2, pi7>=1, pi8>=0, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l + ys0_2*xo2l + ys0_3*xo3l + ys0_4*xo4l + ys0_5*xo5l + ys0_6*xo6l + ys0_7*xo7l + ys0_8*xo8l) * (1 + pi0) + (ys0_1*xo1r + ys0_2*xo2r + ys0_3*xo3r + ys0_4*xo4r + ys0_5*xo5r + ys0_6*xo6r + ys0_7*xo7r + ys0_8*xo8r) * (1 + pi1) + (ys0_1*xo1u + ys0_2*xo2u + ys0_3*xo3u + ys0_4*xo4u + ys0_5*xo5u + ys0_6*xo6u + ys0_7*xo7u + ys0_8*xo8u) * (1 + pi0) + (ys0_1*xo1d + ys0_2*xo2d + ys0_3*xo3d + ys0_4*xo4d + ys0_5*xo5d + ys0_6*xo6d + ys0_7*xo7d + ys0_8*xo8d) * (1 + pi3),
pi1 == (ys1_1*xo1l + ys1_2*xo2l + ys1_3*xo3l + ys1_4*xo4l + ys1_5*xo5l + ys1_6*xo6l + ys1_7*xo7l + ys1_8*xo8l) * (1 + pi0) + (ys1_1*xo1r + ys1_2*xo2r + ys1_3*xo3r + ys1_4*xo4r + ys1_5*xo5r + ys1_6*xo6r + ys1_7*xo7r + ys1_8*xo8r) * (1 + pi2) + (ys1_1*xo1u + ys1_2*xo2u + ys1_3*xo3u + ys1_4*xo4u + ys1_5*xo5u + ys1_6*xo6u + ys1_7*xo7u + ys1_8*xo8u) * (1 + pi1) + (ys1_1*xo1d + ys1_2*xo2d + ys1_3*xo3d + ys1_4*xo4d + ys1_5*xo5d + ys1_6*xo6d + ys1_7*xo7d + ys1_8*xo8d) * (1 + pi4),
pi2 == (ys2_1*xo1l + ys2_2*xo2l + ys2_3*xo3l + ys2_4*xo4l + ys2_5*xo5l + ys2_6*xo6l + ys2_7*xo7l + ys2_8*xo8l) * (1 + pi1) + (ys2_1*xo1r + ys2_2*xo2r + ys2_3*xo3r + ys2_4*xo4r + ys2_5*xo5r + ys2_6*xo6r + ys2_7*xo7r + ys2_8*xo8r) * (1 + pi2) + (ys2_1*xo1u + ys2_2*xo2u + ys2_3*xo3u + ys2_4*xo4u + ys2_5*xo5u + ys2_6*xo6u + ys2_7*xo7u + ys2_8*xo8u) * (1 + pi2) + (ys2_1*xo1d + ys2_2*xo2d + ys2_3*xo3d + ys2_4*xo4d + ys2_5*xo5d + ys2_6*xo6d + ys2_7*xo7d + ys2_8*xo8d) * (1 + pi5),
pi3 == (ys3_1*xo1l + ys3_2*xo2l + ys3_3*xo3l + ys3_4*xo4l + ys3_5*xo5l + ys3_6*xo6l + ys3_7*xo7l + ys3_8*xo8l) * (1 + pi3) + (ys3_1*xo1r + ys3_2*xo2r + ys3_3*xo3r + ys3_4*xo4r + ys3_5*xo5r + ys3_6*xo6r + ys3_7*xo7r + ys3_8*xo8r) * (1 + pi4) + (ys3_1*xo1u + ys3_2*xo2u + ys3_3*xo3u + ys3_4*xo4u + ys3_5*xo5u + ys3_6*xo6u + ys3_7*xo7u + ys3_8*xo8u) * (1 + pi0) + (ys3_1*xo1d + ys3_2*xo2d + ys3_3*xo3d + ys3_4*xo4d + ys3_5*xo5d + ys3_6*xo6d + ys3_7*xo7d + ys3_8*xo8d) * (1 + pi6),
pi4 == (ys4_1*xo1l + ys4_2*xo2l + ys4_3*xo3l + ys4_4*xo4l + ys4_5*xo5l + ys4_6*xo6l + ys4_7*xo7l + ys4_8*xo8l) * (1 + pi3) + (ys4_1*xo1r + ys4_2*xo2r + ys4_3*xo3r + ys4_4*xo4r + ys4_5*xo5r + ys4_6*xo6r + ys4_7*xo7r + ys4_8*xo8r) * (1 + pi5) + (ys4_1*xo1u + ys4_2*xo2u + ys4_3*xo3u + ys4_4*xo4u + ys4_5*xo5u + ys4_6*xo6u + ys4_7*xo7u + ys4_8*xo8u) * (1 + pi1) + (ys4_1*xo1d + ys4_2*xo2d + ys4_3*xo3d + ys4_4*xo4d + ys4_5*xo5d + ys4_6*xo6d + ys4_7*xo7d + ys4_8*xo8d) * (1 + pi7),
pi5 == (ys5_1*xo1l + ys5_2*xo2l + ys5_3*xo3l + ys5_4*xo4l + ys5_5*xo5l + ys5_6*xo6l + ys5_7*xo7l + ys5_8*xo8l) * (1 + pi4) + (ys5_1*xo1r + ys5_2*xo2r + ys5_3*xo3r + ys5_4*xo4r + ys5_5*xo5r + ys5_6*xo6r + ys5_7*xo7r + ys5_8*xo8r) * (1 + pi5) + (ys5_1*xo1u + ys5_2*xo2u + ys5_3*xo3u + ys5_4*xo4u + ys5_5*xo5u + ys5_6*xo6u + ys5_7*xo7u + ys5_8*xo8u) * (1 + pi2) + (ys5_1*xo1d + ys5_2*xo2d + ys5_3*xo3d + ys5_4*xo4d + ys5_5*xo5d + ys5_6*xo6d + ys5_7*xo7d + ys5_8*xo8d) * (1 + pi8),
pi6 == (ys6_1*xo1l + ys6_2*xo2l + ys6_3*xo3l + ys6_4*xo4l + ys6_5*xo5l + ys6_6*xo6l + ys6_7*xo7l + ys6_8*xo8l) * (1 + pi6) + (ys6_1*xo1r + ys6_2*xo2r + ys6_3*xo3r + ys6_4*xo4r + ys6_5*xo5r + ys6_6*xo6r + ys6_7*xo7r + ys6_8*xo8r) * (1 + pi7) + (ys6_1*xo1u + ys6_2*xo2u + ys6_3*xo3u + ys6_4*xo4u + ys6_5*xo5u + ys6_6*xo6u + ys6_7*xo7u + ys6_8*xo8u) * (1 + pi3) + (ys6_1*xo1d + ys6_2*xo2d + ys6_3*xo3d + ys6_4*xo4d + ys6_5*xo5d + ys6_6*xo6d + ys6_7*xo7d + ys6_8*xo8d) * (1 + pi6),
pi7 == (ys7_1*xo1l + ys7_2*xo2l + ys7_3*xo3l + ys7_4*xo4l + ys7_5*xo5l + ys7_6*xo6l + ys7_7*xo7l + ys7_8*xo8l) * (1 + pi6) + (ys7_1*xo1r + ys7_2*xo2r + ys7_3*xo3r + ys7_4*xo4r + ys7_5*xo5r + ys7_6*xo6r + ys7_7*xo7r + ys7_8*xo8r) * (1 + pi8) + (ys7_1*xo1u + ys7_2*xo2u + ys7_3*xo3u + ys7_4*xo4u + ys7_5*xo5u + ys7_6*xo6u + ys7_7*xo7u + ys7_8*xo8u) * (1 + pi4) + (ys7_1*xo1d + ys7_2*xo2d + ys7_3*xo3d + ys7_4*xo4d + ys7_5*xo5d + ys7_6*xo6d + ys7_7*xo7d + ys7_8*xo8d) * (1 + pi7),
pi8 == 0, 
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= 2.25
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7) * Q(1,8) <= 2.25,
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
xo5l>= 0,
xo5l<= 1,
xo5r>= 0,
xo5r<= 1,
xo5u>= 0,
xo5u<= 1,
xo5d>= 0,
xo5d<= 1,
xo6l>= 0,
xo6l<= 1,
xo6r>= 0,
xo6r<= 1,
xo6u>= 0,
xo6u<= 1,
xo6d>= 0,
xo6d<= 1,
xo7l>= 0,
xo7l<= 1,
xo7r>= 0,
xo7r<= 1,
xo7u>= 0,
xo7u<= 1,
xo7d>= 0,
xo7d<= 1,
xo8l>= 0,
xo8l<= 1,
xo8r>= 0,
xo8r<= 1,
xo8u>= 0,
xo8u<= 1,
xo8d>= 0,
xo8d<= 1,
xo1l + xo1r + xo1u + xo1d == 1,
xo2l + xo2r + xo2u + xo2d == 1,
xo3l + xo3r + xo3u + xo3d == 1,
xo4l + xo4r + xo4u + xo4d == 1,
xo5l + xo5r + xo5u + xo5d == 1,
xo6l + xo6r + xo6u + xo6d == 1,
xo7l + xo7r + xo7u + xo7d == 1,
xo8l + xo8r + xo8u + xo8d == 1,
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
Or(xo5l == 0, xo5l == 1),
Or(xo5r == 0, xo5r == 1),
Or(xo5u == 0, xo5u == 1),
Or(xo5d == 0, xo5d == 1),
Or(xo6l == 0, xo6l == 1),
Or(xo6r == 0, xo6r == 1),
Or(xo6u == 0, xo6u == 1),
Or(xo6d == 0, xo6d == 1),
Or(xo7l == 0, xo7l == 1),
Or(xo7r == 0, xo7r == 1),
Or(xo7u == 0, xo7u == 1),
Or(xo7d == 0, xo7d == 1),
Or(xo8l == 0, xo8l == 1),
Or(xo8r == 0, xo8r == 1),
Or(xo8u == 0, xo8u == 1),
Or(xo8d == 0, xo8d == 1),
# ysNM is a function that should map every state N to some observable class M
Or(ys0_1== 0 , ys0_1== 1),
Or(ys0_2== 0 , ys0_2== 1),
Or(ys0_3== 0 , ys0_3== 1),
Or(ys0_4== 0 , ys0_4== 1),
Or(ys0_5== 0 , ys0_5== 1),
Or(ys0_6== 0 , ys0_6== 1),
Or(ys0_7== 0 , ys0_7== 1),
Or(ys0_8== 0 , ys0_8== 1),
Or(ys1_1== 0 , ys1_1== 1),
Or(ys1_2== 0 , ys1_2== 1),
Or(ys1_3== 0 , ys1_3== 1),
Or(ys1_4== 0 , ys1_4== 1),
Or(ys1_5== 0 , ys1_5== 1),
Or(ys1_6== 0 , ys1_6== 1),
Or(ys1_7== 0 , ys1_7== 1),
Or(ys1_8== 0 , ys1_8== 1),
Or(ys2_1== 0 , ys2_1== 1),
Or(ys2_2== 0 , ys2_2== 1),
Or(ys2_3== 0 , ys2_3== 1),
Or(ys2_4== 0 , ys2_4== 1),
Or(ys2_5== 0 , ys2_5== 1),
Or(ys2_6== 0 , ys2_6== 1),
Or(ys2_7== 0 , ys2_7== 1),
Or(ys2_8== 0 , ys2_8== 1),
Or(ys3_1== 0 , ys3_1== 1),
Or(ys3_2== 0 , ys3_2== 1),
Or(ys3_3== 0 , ys3_3== 1),
Or(ys3_4== 0 , ys3_4== 1),
Or(ys3_5== 0 , ys3_5== 1),
Or(ys3_6== 0 , ys3_6== 1),
Or(ys3_7== 0 , ys3_7== 1),
Or(ys3_8== 0 , ys3_8== 1),
Or(ys4_1== 0 , ys4_1== 1),
Or(ys4_2== 0 , ys4_2== 1),
Or(ys4_3== 0 , ys4_3== 1),
Or(ys4_4== 0 , ys4_4== 1),
Or(ys4_5== 0 , ys4_5== 1),
Or(ys4_6== 0 , ys4_6== 1),
Or(ys4_7== 0 , ys4_7== 1),
Or(ys4_8== 0 , ys4_8== 1),
Or(ys5_1== 0 , ys5_1== 1),
Or(ys5_2== 0 , ys5_2== 1),
Or(ys5_3== 0 , ys5_3== 1),
Or(ys5_4== 0 , ys5_4== 1),
Or(ys5_5== 0 , ys5_5== 1),
Or(ys5_6== 0 , ys5_6== 1),
Or(ys5_7== 0 , ys5_7== 1),
Or(ys5_8== 0 , ys5_8== 1),
Or(ys6_1== 0 , ys6_1== 1),
Or(ys6_2== 0 , ys6_2== 1),
Or(ys6_3== 0 , ys6_3== 1),
Or(ys6_4== 0 , ys6_4== 1),
Or(ys6_5== 0 , ys6_5== 1),
Or(ys6_6== 0 , ys6_6== 1),
Or(ys6_7== 0 , ys6_7== 1),
Or(ys6_8== 0 , ys6_8== 1),
Or(ys7_1== 0 , ys7_1== 1),
Or(ys7_2== 0 , ys7_2== 1),
Or(ys7_3== 0 , ys7_3== 1),
Or(ys7_4== 0 , ys7_4== 1),
Or(ys7_5== 0 , ys7_5== 1),
Or(ys7_6== 0 , ys7_6== 1),
Or(ys7_7== 0 , ys7_7== 1),
Or(ys7_8== 0 , ys7_8== 1),
# Every state should be mapped to exactly one equivalence class
ys0_1 + ys0_2 + ys0_3 + ys0_4 + ys0_5 + ys0_6 + ys0_7 + ys0_8 == 1,
ys1_1 + ys1_2 + ys1_3 + ys1_4 + ys1_5 + ys1_6 + ys1_7 + ys1_8 == 1,
ys2_1 + ys2_2 + ys2_3 + ys2_4 + ys2_5 + ys2_6 + ys2_7 + ys2_8 == 1,
ys3_1 + ys3_2 + ys3_3 + ys3_4 + ys3_5 + ys3_6 + ys3_7 + ys3_8 == 1,
ys4_1 + ys4_2 + ys4_3 + ys4_4 + ys4_5 + ys4_6 + ys4_7 + ys4_8 == 1,
ys5_1 + ys5_2 + ys5_3 + ys5_4 + ys5_5 + ys5_6 + ys5_7 + ys5_8 == 1,
ys6_1 + ys6_2 + ys6_3 + ys6_4 + ys6_5 + ys6_6 + ys6_7 + ys6_8 == 1,
ys7_1 + ys7_2 + ys7_3 + ys7_4 + ys7_5 + ys7_6 + ys7_7 + ys7_8 == 1
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
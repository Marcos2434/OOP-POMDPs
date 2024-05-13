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
pi25 = Real('pi25')
pi26 = Real('pi26')
pi27 = Real('pi27')
pi28 = Real('pi28')
pi29 = Real('pi29')
pi30 = Real('pi30')
pi31 = Real('pi31')
pi32 = Real('pi32')
pi33 = Real('pi33')
pi34 = Real('pi34')
pi35 = Real('pi35')
pi36 = Real('pi36')
pi37 = Real('pi37')
pi38 = Real('pi38')
pi39 = Real('pi39')
pi40 = Real('pi40')
pi41 = Real('pi41')
pi42 = Real('pi42')
pi43 = Real('pi43')
pi44 = Real('pi44')
pi45 = Real('pi45')
pi46 = Real('pi46')
pi47 = Real('pi47')
pi48 = Real('pi48')
pi49 = Real('pi49')
pi50 = Real('pi50')
pi51 = Real('pi51')
pi52 = Real('pi52')
pi53 = Real('pi53')
pi54 = Real('pi54')
pi55 = Real('pi55')
pi56 = Real('pi56')
pi57 = Real('pi57')
pi58 = Real('pi58')
pi59 = Real('pi59')
pi60 = Real('pi60')
pi61 = Real('pi61')
pi62 = Real('pi62')
pi63 = Real('pi63')

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
ys21_1 = Real('ys21_1')
ys21_2 = Real('ys21_2')
ys22_1 = Real('ys22_1')
ys22_2 = Real('ys22_2')
ys23_1 = Real('ys23_1')
ys23_2 = Real('ys23_2')
ys24_1 = Real('ys24_1')
ys24_2 = Real('ys24_2')
ys25_1 = Real('ys25_1')
ys25_2 = Real('ys25_2')
ys26_1 = Real('ys26_1')
ys26_2 = Real('ys26_2')
ys27_1 = Real('ys27_1')
ys27_2 = Real('ys27_2')
ys28_1 = Real('ys28_1')
ys28_2 = Real('ys28_2')
ys29_1 = Real('ys29_1')
ys29_2 = Real('ys29_2')
ys30_1 = Real('ys30_1')
ys30_2 = Real('ys30_2')
ys31_1 = Real('ys31_1')
ys31_2 = Real('ys31_2')
ys32_1 = Real('ys32_1')
ys32_2 = Real('ys32_2')
ys33_1 = Real('ys33_1')
ys33_2 = Real('ys33_2')
ys34_1 = Real('ys34_1')
ys34_2 = Real('ys34_2')
ys35_1 = Real('ys35_1')
ys35_2 = Real('ys35_2')
ys36_1 = Real('ys36_1')
ys36_2 = Real('ys36_2')
ys37_1 = Real('ys37_1')
ys37_2 = Real('ys37_2')
ys38_1 = Real('ys38_1')
ys38_2 = Real('ys38_2')
ys39_1 = Real('ys39_1')
ys39_2 = Real('ys39_2')
ys40_1 = Real('ys40_1')
ys40_2 = Real('ys40_2')
ys41_1 = Real('ys41_1')
ys41_2 = Real('ys41_2')
ys42_1 = Real('ys42_1')
ys42_2 = Real('ys42_2')
ys43_1 = Real('ys43_1')
ys43_2 = Real('ys43_2')
ys44_1 = Real('ys44_1')
ys44_2 = Real('ys44_2')
ys45_1 = Real('ys45_1')
ys45_2 = Real('ys45_2')
ys46_1 = Real('ys46_1')
ys46_2 = Real('ys46_2')
ys47_1 = Real('ys47_1')
ys47_2 = Real('ys47_2')
ys48_1 = Real('ys48_1')
ys48_2 = Real('ys48_2')
ys49_1 = Real('ys49_1')
ys49_2 = Real('ys49_2')
ys50_1 = Real('ys50_1')
ys50_2 = Real('ys50_2')
ys51_1 = Real('ys51_1')
ys51_2 = Real('ys51_2')
ys52_1 = Real('ys52_1')
ys52_2 = Real('ys52_2')
ys53_1 = Real('ys53_1')
ys53_2 = Real('ys53_2')
ys54_1 = Real('ys54_1')
ys54_2 = Real('ys54_2')
ys55_1 = Real('ys55_1')
ys55_2 = Real('ys55_2')
ys56_1 = Real('ys56_1')
ys56_2 = Real('ys56_2')
ys57_1 = Real('ys57_1')
ys57_2 = Real('ys57_2')
ys58_1 = Real('ys58_1')
ys58_2 = Real('ys58_2')
ys59_1 = Real('ys59_1')
ys59_2 = Real('ys59_2')
ys60_1 = Real('ys60_1')
ys60_2 = Real('ys60_2')
ys61_1 = Real('ys61_1')
ys61_2 = Real('ys61_2')
ys62_1 = Real('ys62_1')
ys62_2 = Real('ys62_2')
ys63_1 = Real('ys63_1')
ys63_2 = Real('ys63_2')

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
pi0>=1, pi1>=1, pi2>=2, pi3>=3, pi4>=4, pi5>=5, pi6>=6, pi7>=7, pi8>=0, pi9>=1, pi10>=2, pi11>=3, pi12>=4, pi13>=5, pi14>=6, pi15>=7, pi16>=1, pi17>=2, pi18>=3, pi19>=4, pi20>=5, pi21>=6, pi22>=7, pi23>=8, pi24>=2, pi25>=3, pi26>=4, pi27>=5, pi28>=6, pi29>=7, pi30>=8, pi31>=9, pi32>=3, pi33>=4, pi34>=5, pi35>=6, pi36>=7, pi37>=8, pi38>=9, pi39>=10, pi40>=4, pi41>=5, pi42>=6, pi43>=7, pi44>=8, pi45>=9, pi46>=10, pi47>=11, pi48>=5, pi49>=6, pi50>=7, pi51>=8, pi52>=9, pi53>=10, pi54>=11, pi55>=12, pi56>=6, pi57>=7, pi58>=8, pi59>=9, pi60>=10, pi61>=11, pi62>=12, pi63>=13, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l + ys0_2*xo2l) * (1 + pi0) + (ys0_1*xo1r + ys0_2*xo2r) * (1 + pi1) + (ys0_1*xo1u + ys0_2*xo2u) * (1 + pi0) + (ys0_1*xo1d + ys0_2*xo2d) * (1 + pi8),
pi1 == (ys1_1*xo1l + ys1_2*xo2l) * (1 + pi0) + (ys1_1*xo1r + ys1_2*xo2r) * (1 + pi2) + (ys1_1*xo1u + ys1_2*xo2u) * (1 + pi1) + (ys1_1*xo1d + ys1_2*xo2d) * (1 + pi9),
pi2 == (ys2_1*xo1l + ys2_2*xo2l) * (1 + pi1) + (ys2_1*xo1r + ys2_2*xo2r) * (1 + pi3) + (ys2_1*xo1u + ys2_2*xo2u) * (1 + pi2) + (ys2_1*xo1d + ys2_2*xo2d) * (1 + pi10),
pi3 == (ys3_1*xo1l + ys3_2*xo2l) * (1 + pi2) + (ys3_1*xo1r + ys3_2*xo2r) * (1 + pi4) + (ys3_1*xo1u + ys3_2*xo2u) * (1 + pi3) + (ys3_1*xo1d + ys3_2*xo2d) * (1 + pi11),
pi4 == (ys4_1*xo1l + ys4_2*xo2l) * (1 + pi3) + (ys4_1*xo1r + ys4_2*xo2r) * (1 + pi5) + (ys4_1*xo1u + ys4_2*xo2u) * (1 + pi4) + (ys4_1*xo1d + ys4_2*xo2d) * (1 + pi12),
pi5 == (ys5_1*xo1l + ys5_2*xo2l) * (1 + pi4) + (ys5_1*xo1r + ys5_2*xo2r) * (1 + pi6) + (ys5_1*xo1u + ys5_2*xo2u) * (1 + pi5) + (ys5_1*xo1d + ys5_2*xo2d) * (1 + pi13),
pi6 == (ys6_1*xo1l + ys6_2*xo2l) * (1 + pi5) + (ys6_1*xo1r + ys6_2*xo2r) * (1 + pi7) + (ys6_1*xo1u + ys6_2*xo2u) * (1 + pi6) + (ys6_1*xo1d + ys6_2*xo2d) * (1 + pi14),
pi7 == (ys7_1*xo1l + ys7_2*xo2l) * (1 + pi6) + (ys7_1*xo1r + ys7_2*xo2r) * (1 + pi7) + (ys7_1*xo1u + ys7_2*xo2u) * (1 + pi7) + (ys7_1*xo1d + ys7_2*xo2d) * (1 + pi15),
pi8 == 0, 
pi9 == (ys9_1*xo1l + ys9_2*xo2l) * (1 + pi8) + (ys9_1*xo1r + ys9_2*xo2r) * (1 + pi10) + (ys9_1*xo1u + ys9_2*xo2u) * (1 + pi1) + (ys9_1*xo1d + ys9_2*xo2d) * (1 + pi17),
pi10 == (ys10_1*xo1l + ys10_2*xo2l) * (1 + pi9) + (ys10_1*xo1r + ys10_2*xo2r) * (1 + pi11) + (ys10_1*xo1u + ys10_2*xo2u) * (1 + pi2) + (ys10_1*xo1d + ys10_2*xo2d) * (1 + pi18),
pi11 == (ys11_1*xo1l + ys11_2*xo2l) * (1 + pi10) + (ys11_1*xo1r + ys11_2*xo2r) * (1 + pi12) + (ys11_1*xo1u + ys11_2*xo2u) * (1 + pi3) + (ys11_1*xo1d + ys11_2*xo2d) * (1 + pi19),
pi12 == (ys12_1*xo1l + ys12_2*xo2l) * (1 + pi11) + (ys12_1*xo1r + ys12_2*xo2r) * (1 + pi13) + (ys12_1*xo1u + ys12_2*xo2u) * (1 + pi4) + (ys12_1*xo1d + ys12_2*xo2d) * (1 + pi20),
pi13 == (ys13_1*xo1l + ys13_2*xo2l) * (1 + pi12) + (ys13_1*xo1r + ys13_2*xo2r) * (1 + pi14) + (ys13_1*xo1u + ys13_2*xo2u) * (1 + pi5) + (ys13_1*xo1d + ys13_2*xo2d) * (1 + pi21),
pi14 == (ys14_1*xo1l + ys14_2*xo2l) * (1 + pi13) + (ys14_1*xo1r + ys14_2*xo2r) * (1 + pi15) + (ys14_1*xo1u + ys14_2*xo2u) * (1 + pi6) + (ys14_1*xo1d + ys14_2*xo2d) * (1 + pi22),
pi15 == (ys15_1*xo1l + ys15_2*xo2l) * (1 + pi14) + (ys15_1*xo1r + ys15_2*xo2r) * (1 + pi15) + (ys15_1*xo1u + ys15_2*xo2u) * (1 + pi7) + (ys15_1*xo1d + ys15_2*xo2d) * (1 + pi23),
pi16 == (ys16_1*xo1l + ys16_2*xo2l) * (1 + pi16) + (ys16_1*xo1r + ys16_2*xo2r) * (1 + pi17) + (ys16_1*xo1u + ys16_2*xo2u) * (1 + pi8) + (ys16_1*xo1d + ys16_2*xo2d) * (1 + pi24),
pi17 == (ys17_1*xo1l + ys17_2*xo2l) * (1 + pi16) + (ys17_1*xo1r + ys17_2*xo2r) * (1 + pi18) + (ys17_1*xo1u + ys17_2*xo2u) * (1 + pi9) + (ys17_1*xo1d + ys17_2*xo2d) * (1 + pi25),
pi18 == (ys18_1*xo1l + ys18_2*xo2l) * (1 + pi17) + (ys18_1*xo1r + ys18_2*xo2r) * (1 + pi19) + (ys18_1*xo1u + ys18_2*xo2u) * (1 + pi10) + (ys18_1*xo1d + ys18_2*xo2d) * (1 + pi26),
pi19 == (ys19_1*xo1l + ys19_2*xo2l) * (1 + pi18) + (ys19_1*xo1r + ys19_2*xo2r) * (1 + pi20) + (ys19_1*xo1u + ys19_2*xo2u) * (1 + pi11) + (ys19_1*xo1d + ys19_2*xo2d) * (1 + pi27),
pi20 == (ys20_1*xo1l + ys20_2*xo2l) * (1 + pi19) + (ys20_1*xo1r + ys20_2*xo2r) * (1 + pi21) + (ys20_1*xo1u + ys20_2*xo2u) * (1 + pi12) + (ys20_1*xo1d + ys20_2*xo2d) * (1 + pi28),
pi21 == (ys21_1*xo1l + ys21_2*xo2l) * (1 + pi20) + (ys21_1*xo1r + ys21_2*xo2r) * (1 + pi22) + (ys21_1*xo1u + ys21_2*xo2u) * (1 + pi13) + (ys21_1*xo1d + ys21_2*xo2d) * (1 + pi29),
pi22 == (ys22_1*xo1l + ys22_2*xo2l) * (1 + pi21) + (ys22_1*xo1r + ys22_2*xo2r) * (1 + pi23) + (ys22_1*xo1u + ys22_2*xo2u) * (1 + pi14) + (ys22_1*xo1d + ys22_2*xo2d) * (1 + pi30),
pi23 == (ys23_1*xo1l + ys23_2*xo2l) * (1 + pi22) + (ys23_1*xo1r + ys23_2*xo2r) * (1 + pi23) + (ys23_1*xo1u + ys23_2*xo2u) * (1 + pi15) + (ys23_1*xo1d + ys23_2*xo2d) * (1 + pi31),
pi24 == (ys24_1*xo1l + ys24_2*xo2l) * (1 + pi24) + (ys24_1*xo1r + ys24_2*xo2r) * (1 + pi25) + (ys24_1*xo1u + ys24_2*xo2u) * (1 + pi16) + (ys24_1*xo1d + ys24_2*xo2d) * (1 + pi32),
pi25 == (ys25_1*xo1l + ys25_2*xo2l) * (1 + pi24) + (ys25_1*xo1r + ys25_2*xo2r) * (1 + pi26) + (ys25_1*xo1u + ys25_2*xo2u) * (1 + pi17) + (ys25_1*xo1d + ys25_2*xo2d) * (1 + pi33),
pi26 == (ys26_1*xo1l + ys26_2*xo2l) * (1 + pi25) + (ys26_1*xo1r + ys26_2*xo2r) * (1 + pi27) + (ys26_1*xo1u + ys26_2*xo2u) * (1 + pi18) + (ys26_1*xo1d + ys26_2*xo2d) * (1 + pi34),
pi27 == (ys27_1*xo1l + ys27_2*xo2l) * (1 + pi26) + (ys27_1*xo1r + ys27_2*xo2r) * (1 + pi28) + (ys27_1*xo1u + ys27_2*xo2u) * (1 + pi19) + (ys27_1*xo1d + ys27_2*xo2d) * (1 + pi35),
pi28 == (ys28_1*xo1l + ys28_2*xo2l) * (1 + pi27) + (ys28_1*xo1r + ys28_2*xo2r) * (1 + pi29) + (ys28_1*xo1u + ys28_2*xo2u) * (1 + pi20) + (ys28_1*xo1d + ys28_2*xo2d) * (1 + pi36),
pi29 == (ys29_1*xo1l + ys29_2*xo2l) * (1 + pi28) + (ys29_1*xo1r + ys29_2*xo2r) * (1 + pi30) + (ys29_1*xo1u + ys29_2*xo2u) * (1 + pi21) + (ys29_1*xo1d + ys29_2*xo2d) * (1 + pi37),
pi30 == (ys30_1*xo1l + ys30_2*xo2l) * (1 + pi29) + (ys30_1*xo1r + ys30_2*xo2r) * (1 + pi31) + (ys30_1*xo1u + ys30_2*xo2u) * (1 + pi22) + (ys30_1*xo1d + ys30_2*xo2d) * (1 + pi38),
pi31 == (ys31_1*xo1l + ys31_2*xo2l) * (1 + pi30) + (ys31_1*xo1r + ys31_2*xo2r) * (1 + pi31) + (ys31_1*xo1u + ys31_2*xo2u) * (1 + pi23) + (ys31_1*xo1d + ys31_2*xo2d) * (1 + pi39),
pi32 == (ys32_1*xo1l + ys32_2*xo2l) * (1 + pi32) + (ys32_1*xo1r + ys32_2*xo2r) * (1 + pi33) + (ys32_1*xo1u + ys32_2*xo2u) * (1 + pi24) + (ys32_1*xo1d + ys32_2*xo2d) * (1 + pi40),
pi33 == (ys33_1*xo1l + ys33_2*xo2l) * (1 + pi32) + (ys33_1*xo1r + ys33_2*xo2r) * (1 + pi34) + (ys33_1*xo1u + ys33_2*xo2u) * (1 + pi25) + (ys33_1*xo1d + ys33_2*xo2d) * (1 + pi41),
pi34 == (ys34_1*xo1l + ys34_2*xo2l) * (1 + pi33) + (ys34_1*xo1r + ys34_2*xo2r) * (1 + pi35) + (ys34_1*xo1u + ys34_2*xo2u) * (1 + pi26) + (ys34_1*xo1d + ys34_2*xo2d) * (1 + pi42),
pi35 == (ys35_1*xo1l + ys35_2*xo2l) * (1 + pi34) + (ys35_1*xo1r + ys35_2*xo2r) * (1 + pi36) + (ys35_1*xo1u + ys35_2*xo2u) * (1 + pi27) + (ys35_1*xo1d + ys35_2*xo2d) * (1 + pi43),
pi36 == (ys36_1*xo1l + ys36_2*xo2l) * (1 + pi35) + (ys36_1*xo1r + ys36_2*xo2r) * (1 + pi37) + (ys36_1*xo1u + ys36_2*xo2u) * (1 + pi28) + (ys36_1*xo1d + ys36_2*xo2d) * (1 + pi44),
pi37 == (ys37_1*xo1l + ys37_2*xo2l) * (1 + pi36) + (ys37_1*xo1r + ys37_2*xo2r) * (1 + pi38) + (ys37_1*xo1u + ys37_2*xo2u) * (1 + pi29) + (ys37_1*xo1d + ys37_2*xo2d) * (1 + pi45),
pi38 == (ys38_1*xo1l + ys38_2*xo2l) * (1 + pi37) + (ys38_1*xo1r + ys38_2*xo2r) * (1 + pi39) + (ys38_1*xo1u + ys38_2*xo2u) * (1 + pi30) + (ys38_1*xo1d + ys38_2*xo2d) * (1 + pi46),
pi39 == (ys39_1*xo1l + ys39_2*xo2l) * (1 + pi38) + (ys39_1*xo1r + ys39_2*xo2r) * (1 + pi39) + (ys39_1*xo1u + ys39_2*xo2u) * (1 + pi31) + (ys39_1*xo1d + ys39_2*xo2d) * (1 + pi47),
pi40 == (ys40_1*xo1l + ys40_2*xo2l) * (1 + pi40) + (ys40_1*xo1r + ys40_2*xo2r) * (1 + pi41) + (ys40_1*xo1u + ys40_2*xo2u) * (1 + pi32) + (ys40_1*xo1d + ys40_2*xo2d) * (1 + pi48),
pi41 == (ys41_1*xo1l + ys41_2*xo2l) * (1 + pi40) + (ys41_1*xo1r + ys41_2*xo2r) * (1 + pi42) + (ys41_1*xo1u + ys41_2*xo2u) * (1 + pi33) + (ys41_1*xo1d + ys41_2*xo2d) * (1 + pi49),
pi42 == (ys42_1*xo1l + ys42_2*xo2l) * (1 + pi41) + (ys42_1*xo1r + ys42_2*xo2r) * (1 + pi43) + (ys42_1*xo1u + ys42_2*xo2u) * (1 + pi34) + (ys42_1*xo1d + ys42_2*xo2d) * (1 + pi50),
pi43 == (ys43_1*xo1l + ys43_2*xo2l) * (1 + pi42) + (ys43_1*xo1r + ys43_2*xo2r) * (1 + pi44) + (ys43_1*xo1u + ys43_2*xo2u) * (1 + pi35) + (ys43_1*xo1d + ys43_2*xo2d) * (1 + pi51),
pi44 == (ys44_1*xo1l + ys44_2*xo2l) * (1 + pi43) + (ys44_1*xo1r + ys44_2*xo2r) * (1 + pi45) + (ys44_1*xo1u + ys44_2*xo2u) * (1 + pi36) + (ys44_1*xo1d + ys44_2*xo2d) * (1 + pi52),
pi45 == (ys45_1*xo1l + ys45_2*xo2l) * (1 + pi44) + (ys45_1*xo1r + ys45_2*xo2r) * (1 + pi46) + (ys45_1*xo1u + ys45_2*xo2u) * (1 + pi37) + (ys45_1*xo1d + ys45_2*xo2d) * (1 + pi53),
pi46 == (ys46_1*xo1l + ys46_2*xo2l) * (1 + pi45) + (ys46_1*xo1r + ys46_2*xo2r) * (1 + pi47) + (ys46_1*xo1u + ys46_2*xo2u) * (1 + pi38) + (ys46_1*xo1d + ys46_2*xo2d) * (1 + pi54),
pi47 == (ys47_1*xo1l + ys47_2*xo2l) * (1 + pi46) + (ys47_1*xo1r + ys47_2*xo2r) * (1 + pi47) + (ys47_1*xo1u + ys47_2*xo2u) * (1 + pi39) + (ys47_1*xo1d + ys47_2*xo2d) * (1 + pi55),
pi48 == (ys48_1*xo1l + ys48_2*xo2l) * (1 + pi48) + (ys48_1*xo1r + ys48_2*xo2r) * (1 + pi49) + (ys48_1*xo1u + ys48_2*xo2u) * (1 + pi40) + (ys48_1*xo1d + ys48_2*xo2d) * (1 + pi56),
pi49 == (ys49_1*xo1l + ys49_2*xo2l) * (1 + pi48) + (ys49_1*xo1r + ys49_2*xo2r) * (1 + pi50) + (ys49_1*xo1u + ys49_2*xo2u) * (1 + pi41) + (ys49_1*xo1d + ys49_2*xo2d) * (1 + pi57),
pi50 == (ys50_1*xo1l + ys50_2*xo2l) * (1 + pi49) + (ys50_1*xo1r + ys50_2*xo2r) * (1 + pi51) + (ys50_1*xo1u + ys50_2*xo2u) * (1 + pi42) + (ys50_1*xo1d + ys50_2*xo2d) * (1 + pi58),
pi51 == (ys51_1*xo1l + ys51_2*xo2l) * (1 + pi50) + (ys51_1*xo1r + ys51_2*xo2r) * (1 + pi52) + (ys51_1*xo1u + ys51_2*xo2u) * (1 + pi43) + (ys51_1*xo1d + ys51_2*xo2d) * (1 + pi59),
pi52 == (ys52_1*xo1l + ys52_2*xo2l) * (1 + pi51) + (ys52_1*xo1r + ys52_2*xo2r) * (1 + pi53) + (ys52_1*xo1u + ys52_2*xo2u) * (1 + pi44) + (ys52_1*xo1d + ys52_2*xo2d) * (1 + pi60),
pi53 == (ys53_1*xo1l + ys53_2*xo2l) * (1 + pi52) + (ys53_1*xo1r + ys53_2*xo2r) * (1 + pi54) + (ys53_1*xo1u + ys53_2*xo2u) * (1 + pi45) + (ys53_1*xo1d + ys53_2*xo2d) * (1 + pi61),
pi54 == (ys54_1*xo1l + ys54_2*xo2l) * (1 + pi53) + (ys54_1*xo1r + ys54_2*xo2r) * (1 + pi55) + (ys54_1*xo1u + ys54_2*xo2u) * (1 + pi46) + (ys54_1*xo1d + ys54_2*xo2d) * (1 + pi62),
pi55 == (ys55_1*xo1l + ys55_2*xo2l) * (1 + pi54) + (ys55_1*xo1r + ys55_2*xo2r) * (1 + pi55) + (ys55_1*xo1u + ys55_2*xo2u) * (1 + pi47) + (ys55_1*xo1d + ys55_2*xo2d) * (1 + pi63),
pi56 == (ys56_1*xo1l + ys56_2*xo2l) * (1 + pi56) + (ys56_1*xo1r + ys56_2*xo2r) * (1 + pi57) + (ys56_1*xo1u + ys56_2*xo2u) * (1 + pi48) + (ys56_1*xo1d + ys56_2*xo2d) * (1 + pi56),
pi57 == (ys57_1*xo1l + ys57_2*xo2l) * (1 + pi56) + (ys57_1*xo1r + ys57_2*xo2r) * (1 + pi58) + (ys57_1*xo1u + ys57_2*xo2u) * (1 + pi49) + (ys57_1*xo1d + ys57_2*xo2d) * (1 + pi57),
pi58 == (ys58_1*xo1l + ys58_2*xo2l) * (1 + pi57) + (ys58_1*xo1r + ys58_2*xo2r) * (1 + pi59) + (ys58_1*xo1u + ys58_2*xo2u) * (1 + pi50) + (ys58_1*xo1d + ys58_2*xo2d) * (1 + pi58),
pi59 == (ys59_1*xo1l + ys59_2*xo2l) * (1 + pi58) + (ys59_1*xo1r + ys59_2*xo2r) * (1 + pi60) + (ys59_1*xo1u + ys59_2*xo2u) * (1 + pi51) + (ys59_1*xo1d + ys59_2*xo2d) * (1 + pi59),
pi60 == (ys60_1*xo1l + ys60_2*xo2l) * (1 + pi59) + (ys60_1*xo1r + ys60_2*xo2r) * (1 + pi61) + (ys60_1*xo1u + ys60_2*xo2u) * (1 + pi52) + (ys60_1*xo1d + ys60_2*xo2d) * (1 + pi60),
pi61 == (ys61_1*xo1l + ys61_2*xo2l) * (1 + pi60) + (ys61_1*xo1r + ys61_2*xo2r) * (1 + pi62) + (ys61_1*xo1u + ys61_2*xo2u) * (1 + pi53) + (ys61_1*xo1d + ys61_2*xo2d) * (1 + pi61),
pi62 == (ys62_1*xo1l + ys62_2*xo2l) * (1 + pi61) + (ys62_1*xo1r + ys62_2*xo2r) * (1 + pi63) + (ys62_1*xo1u + ys62_2*xo2u) * (1 + pi54) + (ys62_1*xo1d + ys62_2*xo2d) * (1 + pi62),
pi63 == (ys63_1*xo1l + ys63_2*xo2l) * (1 + pi62) + (ys63_1*xo1r + ys63_2*xo2r) * (1 + pi63) + (ys63_1*xo1u + ys63_2*xo2u) * (1 + pi55) + (ys63_1*xo1d + ys63_2*xo2d) * (1 + pi63),
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= 100
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi30+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47+pi48+pi49+pi50+pi51+pi52+pi53+pi54+pi55+pi56+pi57+pi58+pi59+pi60+pi61+pi62+pi63) * Q(1,63) <= 100,
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
# Deterministic Strategies activated
Or(xo1l == 0, xo1l == 1),
Or(xo1r == 0, xo1r == 1),
Or(xo1u == 0, xo1u == 1),
Or(xo1d == 0, xo1d == 1),
Or(xo2l == 0, xo2l == 1),
Or(xo2r == 0, xo2r == 1),
Or(xo2u == 0, xo2u == 1),
Or(xo2d == 0, xo2d == 1),
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
Or(ys21_1== 0 , ys21_1== 1),
Or(ys21_2== 0 , ys21_2== 1),
Or(ys22_1== 0 , ys22_1== 1),
Or(ys22_2== 0 , ys22_2== 1),
Or(ys23_1== 0 , ys23_1== 1),
Or(ys23_2== 0 , ys23_2== 1),
Or(ys24_1== 0 , ys24_1== 1),
Or(ys24_2== 0 , ys24_2== 1),
Or(ys25_1== 0 , ys25_1== 1),
Or(ys25_2== 0 , ys25_2== 1),
Or(ys26_1== 0 , ys26_1== 1),
Or(ys26_2== 0 , ys26_2== 1),
Or(ys27_1== 0 , ys27_1== 1),
Or(ys27_2== 0 , ys27_2== 1),
Or(ys28_1== 0 , ys28_1== 1),
Or(ys28_2== 0 , ys28_2== 1),
Or(ys29_1== 0 , ys29_1== 1),
Or(ys29_2== 0 , ys29_2== 1),
Or(ys30_1== 0 , ys30_1== 1),
Or(ys30_2== 0 , ys30_2== 1),
Or(ys31_1== 0 , ys31_1== 1),
Or(ys31_2== 0 , ys31_2== 1),
Or(ys32_1== 0 , ys32_1== 1),
Or(ys32_2== 0 , ys32_2== 1),
Or(ys33_1== 0 , ys33_1== 1),
Or(ys33_2== 0 , ys33_2== 1),
Or(ys34_1== 0 , ys34_1== 1),
Or(ys34_2== 0 , ys34_2== 1),
Or(ys35_1== 0 , ys35_1== 1),
Or(ys35_2== 0 , ys35_2== 1),
Or(ys36_1== 0 , ys36_1== 1),
Or(ys36_2== 0 , ys36_2== 1),
Or(ys37_1== 0 , ys37_1== 1),
Or(ys37_2== 0 , ys37_2== 1),
Or(ys38_1== 0 , ys38_1== 1),
Or(ys38_2== 0 , ys38_2== 1),
Or(ys39_1== 0 , ys39_1== 1),
Or(ys39_2== 0 , ys39_2== 1),
Or(ys40_1== 0 , ys40_1== 1),
Or(ys40_2== 0 , ys40_2== 1),
Or(ys41_1== 0 , ys41_1== 1),
Or(ys41_2== 0 , ys41_2== 1),
Or(ys42_1== 0 , ys42_1== 1),
Or(ys42_2== 0 , ys42_2== 1),
Or(ys43_1== 0 , ys43_1== 1),
Or(ys43_2== 0 , ys43_2== 1),
Or(ys44_1== 0 , ys44_1== 1),
Or(ys44_2== 0 , ys44_2== 1),
Or(ys45_1== 0 , ys45_1== 1),
Or(ys45_2== 0 , ys45_2== 1),
Or(ys46_1== 0 , ys46_1== 1),
Or(ys46_2== 0 , ys46_2== 1),
Or(ys47_1== 0 , ys47_1== 1),
Or(ys47_2== 0 , ys47_2== 1),
Or(ys48_1== 0 , ys48_1== 1),
Or(ys48_2== 0 , ys48_2== 1),
Or(ys49_1== 0 , ys49_1== 1),
Or(ys49_2== 0 , ys49_2== 1),
Or(ys50_1== 0 , ys50_1== 1),
Or(ys50_2== 0 , ys50_2== 1),
Or(ys51_1== 0 , ys51_1== 1),
Or(ys51_2== 0 , ys51_2== 1),
Or(ys52_1== 0 , ys52_1== 1),
Or(ys52_2== 0 , ys52_2== 1),
Or(ys53_1== 0 , ys53_1== 1),
Or(ys53_2== 0 , ys53_2== 1),
Or(ys54_1== 0 , ys54_1== 1),
Or(ys54_2== 0 , ys54_2== 1),
Or(ys55_1== 0 , ys55_1== 1),
Or(ys55_2== 0 , ys55_2== 1),
Or(ys56_1== 0 , ys56_1== 1),
Or(ys56_2== 0 , ys56_2== 1),
Or(ys57_1== 0 , ys57_1== 1),
Or(ys57_2== 0 , ys57_2== 1),
Or(ys58_1== 0 , ys58_1== 1),
Or(ys58_2== 0 , ys58_2== 1),
Or(ys59_1== 0 , ys59_1== 1),
Or(ys59_2== 0 , ys59_2== 1),
Or(ys60_1== 0 , ys60_1== 1),
Or(ys60_2== 0 , ys60_2== 1),
Or(ys61_1== 0 , ys61_1== 1),
Or(ys61_2== 0 , ys61_2== 1),
Or(ys62_1== 0 , ys62_1== 1),
Or(ys62_2== 0 , ys62_2== 1),
Or(ys63_1== 0 , ys63_1== 1),
Or(ys63_2== 0 , ys63_2== 1),
# Every state should be mapped to exactly one equivalence class
ys0_1 + ys0_2 == 1,
ys1_1 + ys1_2 == 1,
ys2_1 + ys2_2 == 1,
ys3_1 + ys3_2 == 1,
ys4_1 + ys4_2 == 1,
ys5_1 + ys5_2 == 1,
ys6_1 + ys6_2 == 1,
ys7_1 + ys7_2 == 1,
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
ys21_1 + ys21_2 == 1,
ys22_1 + ys22_2 == 1,
ys23_1 + ys23_2 == 1,
ys24_1 + ys24_2 == 1,
ys25_1 + ys25_2 == 1,
ys26_1 + ys26_2 == 1,
ys27_1 + ys27_2 == 1,
ys28_1 + ys28_2 == 1,
ys29_1 + ys29_2 == 1,
ys30_1 + ys30_2 == 1,
ys31_1 + ys31_2 == 1,
ys32_1 + ys32_2 == 1,
ys33_1 + ys33_2 == 1,
ys34_1 + ys34_2 == 1,
ys35_1 + ys35_2 == 1,
ys36_1 + ys36_2 == 1,
ys37_1 + ys37_2 == 1,
ys38_1 + ys38_2 == 1,
ys39_1 + ys39_2 == 1,
ys40_1 + ys40_2 == 1,
ys41_1 + ys41_2 == 1,
ys42_1 + ys42_2 == 1,
ys43_1 + ys43_2 == 1,
ys44_1 + ys44_2 == 1,
ys45_1 + ys45_2 == 1,
ys46_1 + ys46_2 == 1,
ys47_1 + ys47_2 == 1,
ys48_1 + ys48_2 == 1,
ys49_1 + ys49_2 == 1,
ys50_1 + ys50_2 == 1,
ys51_1 + ys51_2 == 1,
ys52_1 + ys52_2 == 1,
ys53_1 + ys53_2 == 1,
ys54_1 + ys54_2 == 1,
ys55_1 + ys55_2 == 1,
ys56_1 + ys56_2 == 1,
ys57_1 + ys57_2 == 1,
ys58_1 + ys58_2 == 1,
ys59_1 + ys59_2 == 1,
ys60_1 + ys60_2 == 1,
ys61_1 + ys61_2 == 1,
ys62_1 + ys62_2 == 1,
ys63_1 + ys63_2 == 1
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
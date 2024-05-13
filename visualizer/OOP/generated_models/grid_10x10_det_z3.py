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
pi64 = Real('pi64')
pi65 = Real('pi65')
pi66 = Real('pi66')
pi67 = Real('pi67')
pi68 = Real('pi68')
pi69 = Real('pi69')
pi70 = Real('pi70')
pi71 = Real('pi71')
pi72 = Real('pi72')
pi73 = Real('pi73')
pi74 = Real('pi74')
pi75 = Real('pi75')
pi76 = Real('pi76')
pi77 = Real('pi77')
pi78 = Real('pi78')
pi79 = Real('pi79')
pi80 = Real('pi80')
pi81 = Real('pi81')
pi82 = Real('pi82')
pi83 = Real('pi83')
pi84 = Real('pi84')
pi85 = Real('pi85')
pi86 = Real('pi86')
pi87 = Real('pi87')
pi88 = Real('pi88')
pi89 = Real('pi89')
pi90 = Real('pi90')
pi91 = Real('pi91')
pi92 = Real('pi92')
pi93 = Real('pi93')
pi94 = Real('pi94')
pi95 = Real('pi95')
pi96 = Real('pi96')
pi97 = Real('pi97')
pi98 = Real('pi98')
pi99 = Real('pi99')

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
ys64_1 = Real('ys64_1')
ys64_2 = Real('ys64_2')
ys65_1 = Real('ys65_1')
ys65_2 = Real('ys65_2')
ys66_1 = Real('ys66_1')
ys66_2 = Real('ys66_2')
ys67_1 = Real('ys67_1')
ys67_2 = Real('ys67_2')
ys68_1 = Real('ys68_1')
ys68_2 = Real('ys68_2')
ys69_1 = Real('ys69_1')
ys69_2 = Real('ys69_2')
ys70_1 = Real('ys70_1')
ys70_2 = Real('ys70_2')
ys71_1 = Real('ys71_1')
ys71_2 = Real('ys71_2')
ys72_1 = Real('ys72_1')
ys72_2 = Real('ys72_2')
ys73_1 = Real('ys73_1')
ys73_2 = Real('ys73_2')
ys74_1 = Real('ys74_1')
ys74_2 = Real('ys74_2')
ys75_1 = Real('ys75_1')
ys75_2 = Real('ys75_2')
ys76_1 = Real('ys76_1')
ys76_2 = Real('ys76_2')
ys77_1 = Real('ys77_1')
ys77_2 = Real('ys77_2')
ys78_1 = Real('ys78_1')
ys78_2 = Real('ys78_2')
ys79_1 = Real('ys79_1')
ys79_2 = Real('ys79_2')
ys80_1 = Real('ys80_1')
ys80_2 = Real('ys80_2')
ys81_1 = Real('ys81_1')
ys81_2 = Real('ys81_2')
ys82_1 = Real('ys82_1')
ys82_2 = Real('ys82_2')
ys83_1 = Real('ys83_1')
ys83_2 = Real('ys83_2')
ys84_1 = Real('ys84_1')
ys84_2 = Real('ys84_2')
ys85_1 = Real('ys85_1')
ys85_2 = Real('ys85_2')
ys86_1 = Real('ys86_1')
ys86_2 = Real('ys86_2')
ys87_1 = Real('ys87_1')
ys87_2 = Real('ys87_2')
ys88_1 = Real('ys88_1')
ys88_2 = Real('ys88_2')
ys89_1 = Real('ys89_1')
ys89_2 = Real('ys89_2')
ys90_1 = Real('ys90_1')
ys90_2 = Real('ys90_2')
ys91_1 = Real('ys91_1')
ys91_2 = Real('ys91_2')
ys92_1 = Real('ys92_1')
ys92_2 = Real('ys92_2')
ys93_1 = Real('ys93_1')
ys93_2 = Real('ys93_2')
ys94_1 = Real('ys94_1')
ys94_2 = Real('ys94_2')
ys95_1 = Real('ys95_1')
ys95_2 = Real('ys95_2')
ys96_1 = Real('ys96_1')
ys96_2 = Real('ys96_2')
ys97_1 = Real('ys97_1')
ys97_2 = Real('ys97_2')
ys98_1 = Real('ys98_1')
ys98_2 = Real('ys98_2')
ys99_1 = Real('ys99_1')
ys99_2 = Real('ys99_2')

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
pi0>=8, pi1>=7, pi2>=6, pi3>=5, pi4>=4, pi5>=3, pi6>=2, pi7>=1, pi8>=0, pi9>=1, pi10>=8, pi11>=7, pi12>=6, pi13>=5, pi14>=4, pi15>=3, pi16>=2, pi17>=1, pi18>=1, pi19>=2, pi20>=9, pi21>=8, pi22>=7, pi23>=6, pi24>=5, pi25>=4, pi26>=3, pi27>=2, pi28>=2, pi29>=3, pi30>=10, pi31>=9, pi32>=8, pi33>=7, pi34>=6, pi35>=5, pi36>=4, pi37>=3, pi38>=3, pi39>=4, pi40>=11, pi41>=10, pi42>=9, pi43>=8, pi44>=7, pi45>=6, pi46>=5, pi47>=4, pi48>=4, pi49>=5, pi50>=12, pi51>=11, pi52>=10, pi53>=9, pi54>=8, pi55>=7, pi56>=6, pi57>=5, pi58>=5, pi59>=6, pi60>=13, pi61>=12, pi62>=11, pi63>=10, pi64>=9, pi65>=8, pi66>=7, pi67>=6, pi68>=6, pi69>=7, pi70>=14, pi71>=13, pi72>=12, pi73>=11, pi74>=10, pi75>=9, pi76>=8, pi77>=7, pi78>=7, pi79>=8, pi80>=15, pi81>=14, pi82>=13, pi83>=12, pi84>=11, pi85>=10, pi86>=9, pi87>=8, pi88>=8, pi89>=9, pi90>=16, pi91>=15, pi92>=14, pi93>=13, pi94>=12, pi95>=11, pi96>=10, pi97>=9, pi98>=9, pi99>=10, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l + ys0_2*xo2l) * (1 + pi0) + (ys0_1*xo1r + ys0_2*xo2r) * (1 + pi1) + (ys0_1*xo1u + ys0_2*xo2u) * (1 + pi0) + (ys0_1*xo1d + ys0_2*xo2d) * (1 + pi10),
pi1 == (ys1_1*xo1l + ys1_2*xo2l) * (1 + pi0) + (ys1_1*xo1r + ys1_2*xo2r) * (1 + pi2) + (ys1_1*xo1u + ys1_2*xo2u) * (1 + pi1) + (ys1_1*xo1d + ys1_2*xo2d) * (1 + pi11),
pi2 == (ys2_1*xo1l + ys2_2*xo2l) * (1 + pi1) + (ys2_1*xo1r + ys2_2*xo2r) * (1 + pi3) + (ys2_1*xo1u + ys2_2*xo2u) * (1 + pi2) + (ys2_1*xo1d + ys2_2*xo2d) * (1 + pi12),
pi3 == (ys3_1*xo1l + ys3_2*xo2l) * (1 + pi2) + (ys3_1*xo1r + ys3_2*xo2r) * (1 + pi4) + (ys3_1*xo1u + ys3_2*xo2u) * (1 + pi3) + (ys3_1*xo1d + ys3_2*xo2d) * (1 + pi13),
pi4 == (ys4_1*xo1l + ys4_2*xo2l) * (1 + pi3) + (ys4_1*xo1r + ys4_2*xo2r) * (1 + pi5) + (ys4_1*xo1u + ys4_2*xo2u) * (1 + pi4) + (ys4_1*xo1d + ys4_2*xo2d) * (1 + pi14),
pi5 == (ys5_1*xo1l + ys5_2*xo2l) * (1 + pi4) + (ys5_1*xo1r + ys5_2*xo2r) * (1 + pi6) + (ys5_1*xo1u + ys5_2*xo2u) * (1 + pi5) + (ys5_1*xo1d + ys5_2*xo2d) * (1 + pi15),
pi6 == (ys6_1*xo1l + ys6_2*xo2l) * (1 + pi5) + (ys6_1*xo1r + ys6_2*xo2r) * (1 + pi7) + (ys6_1*xo1u + ys6_2*xo2u) * (1 + pi6) + (ys6_1*xo1d + ys6_2*xo2d) * (1 + pi16),
pi7 == (ys7_1*xo1l + ys7_2*xo2l) * (1 + pi6) + (ys7_1*xo1r + ys7_2*xo2r) * (1 + pi8) + (ys7_1*xo1u + ys7_2*xo2u) * (1 + pi7) + (ys7_1*xo1d + ys7_2*xo2d) * (1 + pi17),
pi8 == 0, 
pi9 == (ys9_1*xo1l + ys9_2*xo2l) * (1 + pi8) + (ys9_1*xo1r + ys9_2*xo2r) * (1 + pi9) + (ys9_1*xo1u + ys9_2*xo2u) * (1 + pi9) + (ys9_1*xo1d + ys9_2*xo2d) * (1 + pi19),
pi10 == (ys10_1*xo1l + ys10_2*xo2l) * (1 + pi10) + (ys10_1*xo1r + ys10_2*xo2r) * (1 + pi11) + (ys10_1*xo1u + ys10_2*xo2u) * (1 + pi0) + (ys10_1*xo1d + ys10_2*xo2d) * (1 + pi20),
pi11 == (ys11_1*xo1l + ys11_2*xo2l) * (1 + pi10) + (ys11_1*xo1r + ys11_2*xo2r) * (1 + pi12) + (ys11_1*xo1u + ys11_2*xo2u) * (1 + pi1) + (ys11_1*xo1d + ys11_2*xo2d) * (1 + pi21),
pi12 == (ys12_1*xo1l + ys12_2*xo2l) * (1 + pi11) + (ys12_1*xo1r + ys12_2*xo2r) * (1 + pi13) + (ys12_1*xo1u + ys12_2*xo2u) * (1 + pi2) + (ys12_1*xo1d + ys12_2*xo2d) * (1 + pi22),
pi13 == (ys13_1*xo1l + ys13_2*xo2l) * (1 + pi12) + (ys13_1*xo1r + ys13_2*xo2r) * (1 + pi14) + (ys13_1*xo1u + ys13_2*xo2u) * (1 + pi3) + (ys13_1*xo1d + ys13_2*xo2d) * (1 + pi23),
pi14 == (ys14_1*xo1l + ys14_2*xo2l) * (1 + pi13) + (ys14_1*xo1r + ys14_2*xo2r) * (1 + pi15) + (ys14_1*xo1u + ys14_2*xo2u) * (1 + pi4) + (ys14_1*xo1d + ys14_2*xo2d) * (1 + pi24),
pi15 == (ys15_1*xo1l + ys15_2*xo2l) * (1 + pi14) + (ys15_1*xo1r + ys15_2*xo2r) * (1 + pi16) + (ys15_1*xo1u + ys15_2*xo2u) * (1 + pi5) + (ys15_1*xo1d + ys15_2*xo2d) * (1 + pi25),
pi16 == (ys16_1*xo1l + ys16_2*xo2l) * (1 + pi15) + (ys16_1*xo1r + ys16_2*xo2r) * (1 + pi17) + (ys16_1*xo1u + ys16_2*xo2u) * (1 + pi6) + (ys16_1*xo1d + ys16_2*xo2d) * (1 + pi26),
pi17 == (ys17_1*xo1l + ys17_2*xo2l) * (1 + pi16) + (ys17_1*xo1r + ys17_2*xo2r) * (1 + pi18) + (ys17_1*xo1u + ys17_2*xo2u) * (1 + pi7) + (ys17_1*xo1d + ys17_2*xo2d) * (1 + pi27),
pi18 == (ys18_1*xo1l + ys18_2*xo2l) * (1 + pi17) + (ys18_1*xo1r + ys18_2*xo2r) * (1 + pi19) + (ys18_1*xo1u + ys18_2*xo2u) * (1 + pi8) + (ys18_1*xo1d + ys18_2*xo2d) * (1 + pi28),
pi19 == (ys19_1*xo1l + ys19_2*xo2l) * (1 + pi18) + (ys19_1*xo1r + ys19_2*xo2r) * (1 + pi19) + (ys19_1*xo1u + ys19_2*xo2u) * (1 + pi9) + (ys19_1*xo1d + ys19_2*xo2d) * (1 + pi29),
pi20 == (ys20_1*xo1l + ys20_2*xo2l) * (1 + pi20) + (ys20_1*xo1r + ys20_2*xo2r) * (1 + pi21) + (ys20_1*xo1u + ys20_2*xo2u) * (1 + pi10) + (ys20_1*xo1d + ys20_2*xo2d) * (1 + pi30),
pi21 == (ys21_1*xo1l + ys21_2*xo2l) * (1 + pi20) + (ys21_1*xo1r + ys21_2*xo2r) * (1 + pi22) + (ys21_1*xo1u + ys21_2*xo2u) * (1 + pi11) + (ys21_1*xo1d + ys21_2*xo2d) * (1 + pi31),
pi22 == (ys22_1*xo1l + ys22_2*xo2l) * (1 + pi21) + (ys22_1*xo1r + ys22_2*xo2r) * (1 + pi23) + (ys22_1*xo1u + ys22_2*xo2u) * (1 + pi12) + (ys22_1*xo1d + ys22_2*xo2d) * (1 + pi32),
pi23 == (ys23_1*xo1l + ys23_2*xo2l) * (1 + pi22) + (ys23_1*xo1r + ys23_2*xo2r) * (1 + pi24) + (ys23_1*xo1u + ys23_2*xo2u) * (1 + pi13) + (ys23_1*xo1d + ys23_2*xo2d) * (1 + pi33),
pi24 == (ys24_1*xo1l + ys24_2*xo2l) * (1 + pi23) + (ys24_1*xo1r + ys24_2*xo2r) * (1 + pi25) + (ys24_1*xo1u + ys24_2*xo2u) * (1 + pi14) + (ys24_1*xo1d + ys24_2*xo2d) * (1 + pi34),
pi25 == (ys25_1*xo1l + ys25_2*xo2l) * (1 + pi24) + (ys25_1*xo1r + ys25_2*xo2r) * (1 + pi26) + (ys25_1*xo1u + ys25_2*xo2u) * (1 + pi15) + (ys25_1*xo1d + ys25_2*xo2d) * (1 + pi35),
pi26 == (ys26_1*xo1l + ys26_2*xo2l) * (1 + pi25) + (ys26_1*xo1r + ys26_2*xo2r) * (1 + pi27) + (ys26_1*xo1u + ys26_2*xo2u) * (1 + pi16) + (ys26_1*xo1d + ys26_2*xo2d) * (1 + pi36),
pi27 == (ys27_1*xo1l + ys27_2*xo2l) * (1 + pi26) + (ys27_1*xo1r + ys27_2*xo2r) * (1 + pi28) + (ys27_1*xo1u + ys27_2*xo2u) * (1 + pi17) + (ys27_1*xo1d + ys27_2*xo2d) * (1 + pi37),
pi28 == (ys28_1*xo1l + ys28_2*xo2l) * (1 + pi27) + (ys28_1*xo1r + ys28_2*xo2r) * (1 + pi29) + (ys28_1*xo1u + ys28_2*xo2u) * (1 + pi18) + (ys28_1*xo1d + ys28_2*xo2d) * (1 + pi38),
pi29 == (ys29_1*xo1l + ys29_2*xo2l) * (1 + pi28) + (ys29_1*xo1r + ys29_2*xo2r) * (1 + pi29) + (ys29_1*xo1u + ys29_2*xo2u) * (1 + pi19) + (ys29_1*xo1d + ys29_2*xo2d) * (1 + pi39),
pi30 == (ys30_1*xo1l + ys30_2*xo2l) * (1 + pi30) + (ys30_1*xo1r + ys30_2*xo2r) * (1 + pi31) + (ys30_1*xo1u + ys30_2*xo2u) * (1 + pi20) + (ys30_1*xo1d + ys30_2*xo2d) * (1 + pi40),
pi31 == (ys31_1*xo1l + ys31_2*xo2l) * (1 + pi30) + (ys31_1*xo1r + ys31_2*xo2r) * (1 + pi32) + (ys31_1*xo1u + ys31_2*xo2u) * (1 + pi21) + (ys31_1*xo1d + ys31_2*xo2d) * (1 + pi41),
pi32 == (ys32_1*xo1l + ys32_2*xo2l) * (1 + pi31) + (ys32_1*xo1r + ys32_2*xo2r) * (1 + pi33) + (ys32_1*xo1u + ys32_2*xo2u) * (1 + pi22) + (ys32_1*xo1d + ys32_2*xo2d) * (1 + pi42),
pi33 == (ys33_1*xo1l + ys33_2*xo2l) * (1 + pi32) + (ys33_1*xo1r + ys33_2*xo2r) * (1 + pi34) + (ys33_1*xo1u + ys33_2*xo2u) * (1 + pi23) + (ys33_1*xo1d + ys33_2*xo2d) * (1 + pi43),
pi34 == (ys34_1*xo1l + ys34_2*xo2l) * (1 + pi33) + (ys34_1*xo1r + ys34_2*xo2r) * (1 + pi35) + (ys34_1*xo1u + ys34_2*xo2u) * (1 + pi24) + (ys34_1*xo1d + ys34_2*xo2d) * (1 + pi44),
pi35 == (ys35_1*xo1l + ys35_2*xo2l) * (1 + pi34) + (ys35_1*xo1r + ys35_2*xo2r) * (1 + pi36) + (ys35_1*xo1u + ys35_2*xo2u) * (1 + pi25) + (ys35_1*xo1d + ys35_2*xo2d) * (1 + pi45),
pi36 == (ys36_1*xo1l + ys36_2*xo2l) * (1 + pi35) + (ys36_1*xo1r + ys36_2*xo2r) * (1 + pi37) + (ys36_1*xo1u + ys36_2*xo2u) * (1 + pi26) + (ys36_1*xo1d + ys36_2*xo2d) * (1 + pi46),
pi37 == (ys37_1*xo1l + ys37_2*xo2l) * (1 + pi36) + (ys37_1*xo1r + ys37_2*xo2r) * (1 + pi38) + (ys37_1*xo1u + ys37_2*xo2u) * (1 + pi27) + (ys37_1*xo1d + ys37_2*xo2d) * (1 + pi47),
pi38 == (ys38_1*xo1l + ys38_2*xo2l) * (1 + pi37) + (ys38_1*xo1r + ys38_2*xo2r) * (1 + pi39) + (ys38_1*xo1u + ys38_2*xo2u) * (1 + pi28) + (ys38_1*xo1d + ys38_2*xo2d) * (1 + pi48),
pi39 == (ys39_1*xo1l + ys39_2*xo2l) * (1 + pi38) + (ys39_1*xo1r + ys39_2*xo2r) * (1 + pi39) + (ys39_1*xo1u + ys39_2*xo2u) * (1 + pi29) + (ys39_1*xo1d + ys39_2*xo2d) * (1 + pi49),
pi40 == (ys40_1*xo1l + ys40_2*xo2l) * (1 + pi40) + (ys40_1*xo1r + ys40_2*xo2r) * (1 + pi41) + (ys40_1*xo1u + ys40_2*xo2u) * (1 + pi30) + (ys40_1*xo1d + ys40_2*xo2d) * (1 + pi50),
pi41 == (ys41_1*xo1l + ys41_2*xo2l) * (1 + pi40) + (ys41_1*xo1r + ys41_2*xo2r) * (1 + pi42) + (ys41_1*xo1u + ys41_2*xo2u) * (1 + pi31) + (ys41_1*xo1d + ys41_2*xo2d) * (1 + pi51),
pi42 == (ys42_1*xo1l + ys42_2*xo2l) * (1 + pi41) + (ys42_1*xo1r + ys42_2*xo2r) * (1 + pi43) + (ys42_1*xo1u + ys42_2*xo2u) * (1 + pi32) + (ys42_1*xo1d + ys42_2*xo2d) * (1 + pi52),
pi43 == (ys43_1*xo1l + ys43_2*xo2l) * (1 + pi42) + (ys43_1*xo1r + ys43_2*xo2r) * (1 + pi44) + (ys43_1*xo1u + ys43_2*xo2u) * (1 + pi33) + (ys43_1*xo1d + ys43_2*xo2d) * (1 + pi53),
pi44 == (ys44_1*xo1l + ys44_2*xo2l) * (1 + pi43) + (ys44_1*xo1r + ys44_2*xo2r) * (1 + pi45) + (ys44_1*xo1u + ys44_2*xo2u) * (1 + pi34) + (ys44_1*xo1d + ys44_2*xo2d) * (1 + pi54),
pi45 == (ys45_1*xo1l + ys45_2*xo2l) * (1 + pi44) + (ys45_1*xo1r + ys45_2*xo2r) * (1 + pi46) + (ys45_1*xo1u + ys45_2*xo2u) * (1 + pi35) + (ys45_1*xo1d + ys45_2*xo2d) * (1 + pi55),
pi46 == (ys46_1*xo1l + ys46_2*xo2l) * (1 + pi45) + (ys46_1*xo1r + ys46_2*xo2r) * (1 + pi47) + (ys46_1*xo1u + ys46_2*xo2u) * (1 + pi36) + (ys46_1*xo1d + ys46_2*xo2d) * (1 + pi56),
pi47 == (ys47_1*xo1l + ys47_2*xo2l) * (1 + pi46) + (ys47_1*xo1r + ys47_2*xo2r) * (1 + pi48) + (ys47_1*xo1u + ys47_2*xo2u) * (1 + pi37) + (ys47_1*xo1d + ys47_2*xo2d) * (1 + pi57),
pi48 == (ys48_1*xo1l + ys48_2*xo2l) * (1 + pi47) + (ys48_1*xo1r + ys48_2*xo2r) * (1 + pi49) + (ys48_1*xo1u + ys48_2*xo2u) * (1 + pi38) + (ys48_1*xo1d + ys48_2*xo2d) * (1 + pi58),
pi49 == (ys49_1*xo1l + ys49_2*xo2l) * (1 + pi48) + (ys49_1*xo1r + ys49_2*xo2r) * (1 + pi49) + (ys49_1*xo1u + ys49_2*xo2u) * (1 + pi39) + (ys49_1*xo1d + ys49_2*xo2d) * (1 + pi59),
pi50 == (ys50_1*xo1l + ys50_2*xo2l) * (1 + pi50) + (ys50_1*xo1r + ys50_2*xo2r) * (1 + pi51) + (ys50_1*xo1u + ys50_2*xo2u) * (1 + pi40) + (ys50_1*xo1d + ys50_2*xo2d) * (1 + pi60),
pi51 == (ys51_1*xo1l + ys51_2*xo2l) * (1 + pi50) + (ys51_1*xo1r + ys51_2*xo2r) * (1 + pi52) + (ys51_1*xo1u + ys51_2*xo2u) * (1 + pi41) + (ys51_1*xo1d + ys51_2*xo2d) * (1 + pi61),
pi52 == (ys52_1*xo1l + ys52_2*xo2l) * (1 + pi51) + (ys52_1*xo1r + ys52_2*xo2r) * (1 + pi53) + (ys52_1*xo1u + ys52_2*xo2u) * (1 + pi42) + (ys52_1*xo1d + ys52_2*xo2d) * (1 + pi62),
pi53 == (ys53_1*xo1l + ys53_2*xo2l) * (1 + pi52) + (ys53_1*xo1r + ys53_2*xo2r) * (1 + pi54) + (ys53_1*xo1u + ys53_2*xo2u) * (1 + pi43) + (ys53_1*xo1d + ys53_2*xo2d) * (1 + pi63),
pi54 == (ys54_1*xo1l + ys54_2*xo2l) * (1 + pi53) + (ys54_1*xo1r + ys54_2*xo2r) * (1 + pi55) + (ys54_1*xo1u + ys54_2*xo2u) * (1 + pi44) + (ys54_1*xo1d + ys54_2*xo2d) * (1 + pi64),
pi55 == (ys55_1*xo1l + ys55_2*xo2l) * (1 + pi54) + (ys55_1*xo1r + ys55_2*xo2r) * (1 + pi56) + (ys55_1*xo1u + ys55_2*xo2u) * (1 + pi45) + (ys55_1*xo1d + ys55_2*xo2d) * (1 + pi65),
pi56 == (ys56_1*xo1l + ys56_2*xo2l) * (1 + pi55) + (ys56_1*xo1r + ys56_2*xo2r) * (1 + pi57) + (ys56_1*xo1u + ys56_2*xo2u) * (1 + pi46) + (ys56_1*xo1d + ys56_2*xo2d) * (1 + pi66),
pi57 == (ys57_1*xo1l + ys57_2*xo2l) * (1 + pi56) + (ys57_1*xo1r + ys57_2*xo2r) * (1 + pi58) + (ys57_1*xo1u + ys57_2*xo2u) * (1 + pi47) + (ys57_1*xo1d + ys57_2*xo2d) * (1 + pi67),
pi58 == (ys58_1*xo1l + ys58_2*xo2l) * (1 + pi57) + (ys58_1*xo1r + ys58_2*xo2r) * (1 + pi59) + (ys58_1*xo1u + ys58_2*xo2u) * (1 + pi48) + (ys58_1*xo1d + ys58_2*xo2d) * (1 + pi68),
pi59 == (ys59_1*xo1l + ys59_2*xo2l) * (1 + pi58) + (ys59_1*xo1r + ys59_2*xo2r) * (1 + pi59) + (ys59_1*xo1u + ys59_2*xo2u) * (1 + pi49) + (ys59_1*xo1d + ys59_2*xo2d) * (1 + pi69),
pi60 == (ys60_1*xo1l + ys60_2*xo2l) * (1 + pi60) + (ys60_1*xo1r + ys60_2*xo2r) * (1 + pi61) + (ys60_1*xo1u + ys60_2*xo2u) * (1 + pi50) + (ys60_1*xo1d + ys60_2*xo2d) * (1 + pi70),
pi61 == (ys61_1*xo1l + ys61_2*xo2l) * (1 + pi60) + (ys61_1*xo1r + ys61_2*xo2r) * (1 + pi62) + (ys61_1*xo1u + ys61_2*xo2u) * (1 + pi51) + (ys61_1*xo1d + ys61_2*xo2d) * (1 + pi71),
pi62 == (ys62_1*xo1l + ys62_2*xo2l) * (1 + pi61) + (ys62_1*xo1r + ys62_2*xo2r) * (1 + pi63) + (ys62_1*xo1u + ys62_2*xo2u) * (1 + pi52) + (ys62_1*xo1d + ys62_2*xo2d) * (1 + pi72),
pi63 == (ys63_1*xo1l + ys63_2*xo2l) * (1 + pi62) + (ys63_1*xo1r + ys63_2*xo2r) * (1 + pi64) + (ys63_1*xo1u + ys63_2*xo2u) * (1 + pi53) + (ys63_1*xo1d + ys63_2*xo2d) * (1 + pi73),
pi64 == (ys64_1*xo1l + ys64_2*xo2l) * (1 + pi63) + (ys64_1*xo1r + ys64_2*xo2r) * (1 + pi65) + (ys64_1*xo1u + ys64_2*xo2u) * (1 + pi54) + (ys64_1*xo1d + ys64_2*xo2d) * (1 + pi74),
pi65 == (ys65_1*xo1l + ys65_2*xo2l) * (1 + pi64) + (ys65_1*xo1r + ys65_2*xo2r) * (1 + pi66) + (ys65_1*xo1u + ys65_2*xo2u) * (1 + pi55) + (ys65_1*xo1d + ys65_2*xo2d) * (1 + pi75),
pi66 == (ys66_1*xo1l + ys66_2*xo2l) * (1 + pi65) + (ys66_1*xo1r + ys66_2*xo2r) * (1 + pi67) + (ys66_1*xo1u + ys66_2*xo2u) * (1 + pi56) + (ys66_1*xo1d + ys66_2*xo2d) * (1 + pi76),
pi67 == (ys67_1*xo1l + ys67_2*xo2l) * (1 + pi66) + (ys67_1*xo1r + ys67_2*xo2r) * (1 + pi68) + (ys67_1*xo1u + ys67_2*xo2u) * (1 + pi57) + (ys67_1*xo1d + ys67_2*xo2d) * (1 + pi77),
pi68 == (ys68_1*xo1l + ys68_2*xo2l) * (1 + pi67) + (ys68_1*xo1r + ys68_2*xo2r) * (1 + pi69) + (ys68_1*xo1u + ys68_2*xo2u) * (1 + pi58) + (ys68_1*xo1d + ys68_2*xo2d) * (1 + pi78),
pi69 == (ys69_1*xo1l + ys69_2*xo2l) * (1 + pi68) + (ys69_1*xo1r + ys69_2*xo2r) * (1 + pi69) + (ys69_1*xo1u + ys69_2*xo2u) * (1 + pi59) + (ys69_1*xo1d + ys69_2*xo2d) * (1 + pi79),
pi70 == (ys70_1*xo1l + ys70_2*xo2l) * (1 + pi70) + (ys70_1*xo1r + ys70_2*xo2r) * (1 + pi71) + (ys70_1*xo1u + ys70_2*xo2u) * (1 + pi60) + (ys70_1*xo1d + ys70_2*xo2d) * (1 + pi80),
pi71 == (ys71_1*xo1l + ys71_2*xo2l) * (1 + pi70) + (ys71_1*xo1r + ys71_2*xo2r) * (1 + pi72) + (ys71_1*xo1u + ys71_2*xo2u) * (1 + pi61) + (ys71_1*xo1d + ys71_2*xo2d) * (1 + pi81),
pi72 == (ys72_1*xo1l + ys72_2*xo2l) * (1 + pi71) + (ys72_1*xo1r + ys72_2*xo2r) * (1 + pi73) + (ys72_1*xo1u + ys72_2*xo2u) * (1 + pi62) + (ys72_1*xo1d + ys72_2*xo2d) * (1 + pi82),
pi73 == (ys73_1*xo1l + ys73_2*xo2l) * (1 + pi72) + (ys73_1*xo1r + ys73_2*xo2r) * (1 + pi74) + (ys73_1*xo1u + ys73_2*xo2u) * (1 + pi63) + (ys73_1*xo1d + ys73_2*xo2d) * (1 + pi83),
pi74 == (ys74_1*xo1l + ys74_2*xo2l) * (1 + pi73) + (ys74_1*xo1r + ys74_2*xo2r) * (1 + pi75) + (ys74_1*xo1u + ys74_2*xo2u) * (1 + pi64) + (ys74_1*xo1d + ys74_2*xo2d) * (1 + pi84),
pi75 == (ys75_1*xo1l + ys75_2*xo2l) * (1 + pi74) + (ys75_1*xo1r + ys75_2*xo2r) * (1 + pi76) + (ys75_1*xo1u + ys75_2*xo2u) * (1 + pi65) + (ys75_1*xo1d + ys75_2*xo2d) * (1 + pi85),
pi76 == (ys76_1*xo1l + ys76_2*xo2l) * (1 + pi75) + (ys76_1*xo1r + ys76_2*xo2r) * (1 + pi77) + (ys76_1*xo1u + ys76_2*xo2u) * (1 + pi66) + (ys76_1*xo1d + ys76_2*xo2d) * (1 + pi86),
pi77 == (ys77_1*xo1l + ys77_2*xo2l) * (1 + pi76) + (ys77_1*xo1r + ys77_2*xo2r) * (1 + pi78) + (ys77_1*xo1u + ys77_2*xo2u) * (1 + pi67) + (ys77_1*xo1d + ys77_2*xo2d) * (1 + pi87),
pi78 == (ys78_1*xo1l + ys78_2*xo2l) * (1 + pi77) + (ys78_1*xo1r + ys78_2*xo2r) * (1 + pi79) + (ys78_1*xo1u + ys78_2*xo2u) * (1 + pi68) + (ys78_1*xo1d + ys78_2*xo2d) * (1 + pi88),
pi79 == (ys79_1*xo1l + ys79_2*xo2l) * (1 + pi78) + (ys79_1*xo1r + ys79_2*xo2r) * (1 + pi79) + (ys79_1*xo1u + ys79_2*xo2u) * (1 + pi69) + (ys79_1*xo1d + ys79_2*xo2d) * (1 + pi89),
pi80 == (ys80_1*xo1l + ys80_2*xo2l) * (1 + pi80) + (ys80_1*xo1r + ys80_2*xo2r) * (1 + pi81) + (ys80_1*xo1u + ys80_2*xo2u) * (1 + pi70) + (ys80_1*xo1d + ys80_2*xo2d) * (1 + pi90),
pi81 == (ys81_1*xo1l + ys81_2*xo2l) * (1 + pi80) + (ys81_1*xo1r + ys81_2*xo2r) * (1 + pi82) + (ys81_1*xo1u + ys81_2*xo2u) * (1 + pi71) + (ys81_1*xo1d + ys81_2*xo2d) * (1 + pi91),
pi82 == (ys82_1*xo1l + ys82_2*xo2l) * (1 + pi81) + (ys82_1*xo1r + ys82_2*xo2r) * (1 + pi83) + (ys82_1*xo1u + ys82_2*xo2u) * (1 + pi72) + (ys82_1*xo1d + ys82_2*xo2d) * (1 + pi92),
pi83 == (ys83_1*xo1l + ys83_2*xo2l) * (1 + pi82) + (ys83_1*xo1r + ys83_2*xo2r) * (1 + pi84) + (ys83_1*xo1u + ys83_2*xo2u) * (1 + pi73) + (ys83_1*xo1d + ys83_2*xo2d) * (1 + pi93),
pi84 == (ys84_1*xo1l + ys84_2*xo2l) * (1 + pi83) + (ys84_1*xo1r + ys84_2*xo2r) * (1 + pi85) + (ys84_1*xo1u + ys84_2*xo2u) * (1 + pi74) + (ys84_1*xo1d + ys84_2*xo2d) * (1 + pi94),
pi85 == (ys85_1*xo1l + ys85_2*xo2l) * (1 + pi84) + (ys85_1*xo1r + ys85_2*xo2r) * (1 + pi86) + (ys85_1*xo1u + ys85_2*xo2u) * (1 + pi75) + (ys85_1*xo1d + ys85_2*xo2d) * (1 + pi95),
pi86 == (ys86_1*xo1l + ys86_2*xo2l) * (1 + pi85) + (ys86_1*xo1r + ys86_2*xo2r) * (1 + pi87) + (ys86_1*xo1u + ys86_2*xo2u) * (1 + pi76) + (ys86_1*xo1d + ys86_2*xo2d) * (1 + pi96),
pi87 == (ys87_1*xo1l + ys87_2*xo2l) * (1 + pi86) + (ys87_1*xo1r + ys87_2*xo2r) * (1 + pi88) + (ys87_1*xo1u + ys87_2*xo2u) * (1 + pi77) + (ys87_1*xo1d + ys87_2*xo2d) * (1 + pi97),
pi88 == (ys88_1*xo1l + ys88_2*xo2l) * (1 + pi87) + (ys88_1*xo1r + ys88_2*xo2r) * (1 + pi89) + (ys88_1*xo1u + ys88_2*xo2u) * (1 + pi78) + (ys88_1*xo1d + ys88_2*xo2d) * (1 + pi98),
pi89 == (ys89_1*xo1l + ys89_2*xo2l) * (1 + pi88) + (ys89_1*xo1r + ys89_2*xo2r) * (1 + pi89) + (ys89_1*xo1u + ys89_2*xo2u) * (1 + pi79) + (ys89_1*xo1d + ys89_2*xo2d) * (1 + pi99),
pi90 == (ys90_1*xo1l + ys90_2*xo2l) * (1 + pi90) + (ys90_1*xo1r + ys90_2*xo2r) * (1 + pi91) + (ys90_1*xo1u + ys90_2*xo2u) * (1 + pi80) + (ys90_1*xo1d + ys90_2*xo2d) * (1 + pi90),
pi91 == (ys91_1*xo1l + ys91_2*xo2l) * (1 + pi90) + (ys91_1*xo1r + ys91_2*xo2r) * (1 + pi92) + (ys91_1*xo1u + ys91_2*xo2u) * (1 + pi81) + (ys91_1*xo1d + ys91_2*xo2d) * (1 + pi91),
pi92 == (ys92_1*xo1l + ys92_2*xo2l) * (1 + pi91) + (ys92_1*xo1r + ys92_2*xo2r) * (1 + pi93) + (ys92_1*xo1u + ys92_2*xo2u) * (1 + pi82) + (ys92_1*xo1d + ys92_2*xo2d) * (1 + pi92),
pi93 == (ys93_1*xo1l + ys93_2*xo2l) * (1 + pi92) + (ys93_1*xo1r + ys93_2*xo2r) * (1 + pi94) + (ys93_1*xo1u + ys93_2*xo2u) * (1 + pi83) + (ys93_1*xo1d + ys93_2*xo2d) * (1 + pi93),
pi94 == (ys94_1*xo1l + ys94_2*xo2l) * (1 + pi93) + (ys94_1*xo1r + ys94_2*xo2r) * (1 + pi95) + (ys94_1*xo1u + ys94_2*xo2u) * (1 + pi84) + (ys94_1*xo1d + ys94_2*xo2d) * (1 + pi94),
pi95 == (ys95_1*xo1l + ys95_2*xo2l) * (1 + pi94) + (ys95_1*xo1r + ys95_2*xo2r) * (1 + pi96) + (ys95_1*xo1u + ys95_2*xo2u) * (1 + pi85) + (ys95_1*xo1d + ys95_2*xo2d) * (1 + pi95),
pi96 == (ys96_1*xo1l + ys96_2*xo2l) * (1 + pi95) + (ys96_1*xo1r + ys96_2*xo2r) * (1 + pi97) + (ys96_1*xo1u + ys96_2*xo2u) * (1 + pi86) + (ys96_1*xo1d + ys96_2*xo2d) * (1 + pi96),
pi97 == (ys97_1*xo1l + ys97_2*xo2l) * (1 + pi96) + (ys97_1*xo1r + ys97_2*xo2r) * (1 + pi98) + (ys97_1*xo1u + ys97_2*xo2u) * (1 + pi87) + (ys97_1*xo1d + ys97_2*xo2d) * (1 + pi97),
pi98 == (ys98_1*xo1l + ys98_2*xo2l) * (1 + pi97) + (ys98_1*xo1r + ys98_2*xo2r) * (1 + pi99) + (ys98_1*xo1u + ys98_2*xo2u) * (1 + pi88) + (ys98_1*xo1d + ys98_2*xo2d) * (1 + pi98),
pi99 == (ys99_1*xo1l + ys99_2*xo2l) * (1 + pi98) + (ys99_1*xo1r + ys99_2*xo2r) * (1 + pi99) + (ys99_1*xo1u + ys99_2*xo2u) * (1 + pi89) + (ys99_1*xo1d + ys99_2*xo2d) * (1 + pi99),
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= 2.25
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi30+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47+pi48+pi49+pi50+pi51+pi52+pi53+pi54+pi55+pi56+pi57+pi58+pi59+pi60+pi61+pi62+pi63+pi64+pi65+pi66+pi67+pi68+pi69+pi70+pi71+pi72+pi73+pi74+pi75+pi76+pi77+pi78+pi79+pi80+pi81+pi82+pi83+pi84+pi85+pi86+pi87+pi88+pi89+pi90+pi91+pi92+pi93+pi94+pi95+pi96+pi97+pi98+pi99) * Q(1,99) <= 2.25,
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
Or(ys64_1== 0 , ys64_1== 1),
Or(ys64_2== 0 , ys64_2== 1),
Or(ys65_1== 0 , ys65_1== 1),
Or(ys65_2== 0 , ys65_2== 1),
Or(ys66_1== 0 , ys66_1== 1),
Or(ys66_2== 0 , ys66_2== 1),
Or(ys67_1== 0 , ys67_1== 1),
Or(ys67_2== 0 , ys67_2== 1),
Or(ys68_1== 0 , ys68_1== 1),
Or(ys68_2== 0 , ys68_2== 1),
Or(ys69_1== 0 , ys69_1== 1),
Or(ys69_2== 0 , ys69_2== 1),
Or(ys70_1== 0 , ys70_1== 1),
Or(ys70_2== 0 , ys70_2== 1),
Or(ys71_1== 0 , ys71_1== 1),
Or(ys71_2== 0 , ys71_2== 1),
Or(ys72_1== 0 , ys72_1== 1),
Or(ys72_2== 0 , ys72_2== 1),
Or(ys73_1== 0 , ys73_1== 1),
Or(ys73_2== 0 , ys73_2== 1),
Or(ys74_1== 0 , ys74_1== 1),
Or(ys74_2== 0 , ys74_2== 1),
Or(ys75_1== 0 , ys75_1== 1),
Or(ys75_2== 0 , ys75_2== 1),
Or(ys76_1== 0 , ys76_1== 1),
Or(ys76_2== 0 , ys76_2== 1),
Or(ys77_1== 0 , ys77_1== 1),
Or(ys77_2== 0 , ys77_2== 1),
Or(ys78_1== 0 , ys78_1== 1),
Or(ys78_2== 0 , ys78_2== 1),
Or(ys79_1== 0 , ys79_1== 1),
Or(ys79_2== 0 , ys79_2== 1),
Or(ys80_1== 0 , ys80_1== 1),
Or(ys80_2== 0 , ys80_2== 1),
Or(ys81_1== 0 , ys81_1== 1),
Or(ys81_2== 0 , ys81_2== 1),
Or(ys82_1== 0 , ys82_1== 1),
Or(ys82_2== 0 , ys82_2== 1),
Or(ys83_1== 0 , ys83_1== 1),
Or(ys83_2== 0 , ys83_2== 1),
Or(ys84_1== 0 , ys84_1== 1),
Or(ys84_2== 0 , ys84_2== 1),
Or(ys85_1== 0 , ys85_1== 1),
Or(ys85_2== 0 , ys85_2== 1),
Or(ys86_1== 0 , ys86_1== 1),
Or(ys86_2== 0 , ys86_2== 1),
Or(ys87_1== 0 , ys87_1== 1),
Or(ys87_2== 0 , ys87_2== 1),
Or(ys88_1== 0 , ys88_1== 1),
Or(ys88_2== 0 , ys88_2== 1),
Or(ys89_1== 0 , ys89_1== 1),
Or(ys89_2== 0 , ys89_2== 1),
Or(ys90_1== 0 , ys90_1== 1),
Or(ys90_2== 0 , ys90_2== 1),
Or(ys91_1== 0 , ys91_1== 1),
Or(ys91_2== 0 , ys91_2== 1),
Or(ys92_1== 0 , ys92_1== 1),
Or(ys92_2== 0 , ys92_2== 1),
Or(ys93_1== 0 , ys93_1== 1),
Or(ys93_2== 0 , ys93_2== 1),
Or(ys94_1== 0 , ys94_1== 1),
Or(ys94_2== 0 , ys94_2== 1),
Or(ys95_1== 0 , ys95_1== 1),
Or(ys95_2== 0 , ys95_2== 1),
Or(ys96_1== 0 , ys96_1== 1),
Or(ys96_2== 0 , ys96_2== 1),
Or(ys97_1== 0 , ys97_1== 1),
Or(ys97_2== 0 , ys97_2== 1),
Or(ys98_1== 0 , ys98_1== 1),
Or(ys98_2== 0 , ys98_2== 1),
Or(ys99_1== 0 , ys99_1== 1),
Or(ys99_2== 0 , ys99_2== 1),
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
ys63_1 + ys63_2 == 1,
ys64_1 + ys64_2 == 1,
ys65_1 + ys65_2 == 1,
ys66_1 + ys66_2 == 1,
ys67_1 + ys67_2 == 1,
ys68_1 + ys68_2 == 1,
ys69_1 + ys69_2 == 1,
ys70_1 + ys70_2 == 1,
ys71_1 + ys71_2 == 1,
ys72_1 + ys72_2 == 1,
ys73_1 + ys73_2 == 1,
ys74_1 + ys74_2 == 1,
ys75_1 + ys75_2 == 1,
ys76_1 + ys76_2 == 1,
ys77_1 + ys77_2 == 1,
ys78_1 + ys78_2 == 1,
ys79_1 + ys79_2 == 1,
ys80_1 + ys80_2 == 1,
ys81_1 + ys81_2 == 1,
ys82_1 + ys82_2 == 1,
ys83_1 + ys83_2 == 1,
ys84_1 + ys84_2 == 1,
ys85_1 + ys85_2 == 1,
ys86_1 + ys86_2 == 1,
ys87_1 + ys87_2 == 1,
ys88_1 + ys88_2 == 1,
ys89_1 + ys89_2 == 1,
ys90_1 + ys90_2 == 1,
ys91_1 + ys91_2 == 1,
ys92_1 + ys92_2 == 1,
ys93_1 + ys93_2 == 1,
ys94_1 + ys94_2 == 1,
ys95_1 + ys95_2 == 1,
ys96_1 + ys96_2 == 1,
ys97_1 + ys97_2 == 1,
ys98_1 + ys98_2 == 1,
ys99_1 + ys99_2 == 1
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
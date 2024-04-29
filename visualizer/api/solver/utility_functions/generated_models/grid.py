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
ys25_1 = Real('ys25_1')
ys26_1 = Real('ys26_1')
ys27_1 = Real('ys27_1')
ys28_1 = Real('ys28_1')
ys29_1 = Real('ys29_1')
ys30_1 = Real('ys30_1')
ys31_1 = Real('ys31_1')
ys32_1 = Real('ys32_1')
ys33_1 = Real('ys33_1')
ys34_1 = Real('ys34_1')
ys35_1 = Real('ys35_1')
ys36_1 = Real('ys36_1')
ys37_1 = Real('ys37_1')
ys38_1 = Real('ys38_1')
ys39_1 = Real('ys39_1')
ys40_1 = Real('ys40_1')
ys41_1 = Real('ys41_1')
ys42_1 = Real('ys42_1')
ys43_1 = Real('ys43_1')
ys44_1 = Real('ys44_1')
ys45_1 = Real('ys45_1')
ys46_1 = Real('ys46_1')
ys47_1 = Real('ys47_1')
ys48_1 = Real('ys48_1')
ys49_1 = Real('ys49_1')
ys50_1 = Real('ys50_1')
ys51_1 = Real('ys51_1')
ys52_1 = Real('ys52_1')
ys53_1 = Real('ys53_1')
ys54_1 = Real('ys54_1')
ys55_1 = Real('ys55_1')
ys56_1 = Real('ys56_1')
ys57_1 = Real('ys57_1')
ys58_1 = Real('ys58_1')
ys59_1 = Real('ys59_1')
ys60_1 = Real('ys60_1')
ys61_1 = Real('ys61_1')
ys62_1 = Real('ys62_1')
ys63_1 = Real('ys63_1')
ys64_1 = Real('ys64_1')
ys65_1 = Real('ys65_1')
ys66_1 = Real('ys66_1')
ys67_1 = Real('ys67_1')
ys68_1 = Real('ys68_1')
ys69_1 = Real('ys69_1')
ys70_1 = Real('ys70_1')
ys71_1 = Real('ys71_1')
ys72_1 = Real('ys72_1')
ys73_1 = Real('ys73_1')
ys74_1 = Real('ys74_1')
ys75_1 = Real('ys75_1')
ys76_1 = Real('ys76_1')
ys77_1 = Real('ys77_1')
ys78_1 = Real('ys78_1')
ys79_1 = Real('ys79_1')
ys80_1 = Real('ys80_1')
ys81_1 = Real('ys81_1')
ys82_1 = Real('ys82_1')
ys83_1 = Real('ys83_1')
ys84_1 = Real('ys84_1')
ys85_1 = Real('ys85_1')
ys86_1 = Real('ys86_1')
ys87_1 = Real('ys87_1')
ys88_1 = Real('ys88_1')
ys89_1 = Real('ys89_1')
ys90_1 = Real('ys90_1')
ys91_1 = Real('ys91_1')
ys92_1 = Real('ys92_1')
ys93_1 = Real('ys93_1')
ys94_1 = Real('ys94_1')
ys95_1 = Real('ys95_1')
ys96_1 = Real('ys96_1')
ys97_1 = Real('ys97_1')
ys98_1 = Real('ys98_1')
ys99_1 = Real('ys99_1')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo1u = Real('xo1u')
xo1d = Real('xo1d')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=14, pi1>=13, pi2>=12, pi3>=11, pi4>=10, pi5>=9, pi6>=9, pi7>=10, pi8>=11, pi9>=12, pi10>=13, pi11>=12, pi12>=11, pi13>=10, pi14>=9, pi15>=8, pi16>=8, pi17>=9, pi18>=10, pi19>=11, pi20>=12, pi21>=11, pi22>=10, pi23>=9, pi24>=8, pi25>=7, pi26>=7, pi27>=8, pi28>=9, pi29>=10, pi30>=11, pi31>=10, pi32>=9, pi33>=8, pi34>=7, pi35>=6, pi36>=6, pi37>=7, pi38>=8, pi39>=9, pi40>=10, pi41>=9, pi42>=8, pi43>=7, pi44>=6, pi45>=5, pi46>=5, pi47>=6, pi48>=7, pi49>=8, pi50>=9, pi51>=8, pi52>=7, pi53>=6, pi54>=5, pi55>=4, pi56>=4, pi57>=5, pi58>=6, pi59>=7, pi60>=8, pi61>=7, pi62>=6, pi63>=5, pi64>=4, pi65>=3, pi66>=3, pi67>=4, pi68>=5, pi69>=6, pi70>=7, pi71>=6, pi72>=5, pi73>=4, pi74>=3, pi75>=2, pi76>=2, pi77>=3, pi78>=4, pi79>=5, pi80>=6, pi81>=5, pi82>=4, pi83>=3, pi84>=2, pi85>=1, pi86>=1, pi87>=2, pi88>=3, pi89>=4, pi90>=5, pi91>=4, pi92>=3, pi93>=2, pi94>=1, pi95>=0, pi96>=1, pi97>=2, pi98>=3, pi99>=4, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l) * (1 + pi0) + (ys0_1*xo1r) * (1 + pi1) + (ys0_1*xo1u) * (1 + pi0) + (ys0_1*xo1d) * (1 + pi10),
pi1 == (ys1_1*xo1l) * (1 + pi0) + (ys1_1*xo1r) * (1 + pi2) + (ys1_1*xo1u) * (1 + pi1) + (ys1_1*xo1d) * (1 + pi11),
pi2 == (ys2_1*xo1l) * (1 + pi1) + (ys2_1*xo1r) * (1 + pi3) + (ys2_1*xo1u) * (1 + pi2) + (ys2_1*xo1d) * (1 + pi12),
pi3 == (ys3_1*xo1l) * (1 + pi2) + (ys3_1*xo1r) * (1 + pi4) + (ys3_1*xo1u) * (1 + pi3) + (ys3_1*xo1d) * (1 + pi13),
pi4 == (ys4_1*xo1l) * (1 + pi3) + (ys4_1*xo1r) * (1 + pi5) + (ys4_1*xo1u) * (1 + pi4) + (ys4_1*xo1d) * (1 + pi14),
pi5 == (ys5_1*xo1l) * (1 + pi4) + (ys5_1*xo1r) * (1 + pi6) + (ys5_1*xo1u) * (1 + pi5) + (ys5_1*xo1d) * (1 + pi15),
pi6 == (ys6_1*xo1l) * (1 + pi5) + (ys6_1*xo1r) * (1 + pi7) + (ys6_1*xo1u) * (1 + pi6) + (ys6_1*xo1d) * (1 + pi16),
pi7 == (ys7_1*xo1l) * (1 + pi6) + (ys7_1*xo1r) * (1 + pi8) + (ys7_1*xo1u) * (1 + pi7) + (ys7_1*xo1d) * (1 + pi17),
pi8 == (ys8_1*xo1l) * (1 + pi7) + (ys8_1*xo1r) * (1 + pi9) + (ys8_1*xo1u) * (1 + pi8) + (ys8_1*xo1d) * (1 + pi18),
pi9 == (ys9_1*xo1l) * (1 + pi8) + (ys9_1*xo1r) * (1 + pi9) + (ys9_1*xo1u) * (1 + pi9) + (ys9_1*xo1d) * (1 + pi19),
pi10 == (ys10_1*xo1l) * (1 + pi10) + (ys10_1*xo1r) * (1 + pi11) + (ys10_1*xo1u) * (1 + pi0) + (ys10_1*xo1d) * (1 + pi20),
pi11 == (ys11_1*xo1l) * (1 + pi10) + (ys11_1*xo1r) * (1 + pi12) + (ys11_1*xo1u) * (1 + pi1) + (ys11_1*xo1d) * (1 + pi21),
pi12 == (ys12_1*xo1l) * (1 + pi11) + (ys12_1*xo1r) * (1 + pi13) + (ys12_1*xo1u) * (1 + pi2) + (ys12_1*xo1d) * (1 + pi22),
pi13 == (ys13_1*xo1l) * (1 + pi12) + (ys13_1*xo1r) * (1 + pi14) + (ys13_1*xo1u) * (1 + pi3) + (ys13_1*xo1d) * (1 + pi23),
pi14 == (ys14_1*xo1l) * (1 + pi13) + (ys14_1*xo1r) * (1 + pi15) + (ys14_1*xo1u) * (1 + pi4) + (ys14_1*xo1d) * (1 + pi24),
pi15 == (ys15_1*xo1l) * (1 + pi14) + (ys15_1*xo1r) * (1 + pi16) + (ys15_1*xo1u) * (1 + pi5) + (ys15_1*xo1d) * (1 + pi25),
pi16 == (ys16_1*xo1l) * (1 + pi15) + (ys16_1*xo1r) * (1 + pi17) + (ys16_1*xo1u) * (1 + pi6) + (ys16_1*xo1d) * (1 + pi26),
pi17 == (ys17_1*xo1l) * (1 + pi16) + (ys17_1*xo1r) * (1 + pi18) + (ys17_1*xo1u) * (1 + pi7) + (ys17_1*xo1d) * (1 + pi27),
pi18 == (ys18_1*xo1l) * (1 + pi17) + (ys18_1*xo1r) * (1 + pi19) + (ys18_1*xo1u) * (1 + pi8) + (ys18_1*xo1d) * (1 + pi28),
pi19 == (ys19_1*xo1l) * (1 + pi18) + (ys19_1*xo1r) * (1 + pi19) + (ys19_1*xo1u) * (1 + pi9) + (ys19_1*xo1d) * (1 + pi29),
pi20 == (ys20_1*xo1l) * (1 + pi20) + (ys20_1*xo1r) * (1 + pi21) + (ys20_1*xo1u) * (1 + pi10) + (ys20_1*xo1d) * (1 + pi30),
pi21 == (ys21_1*xo1l) * (1 + pi20) + (ys21_1*xo1r) * (1 + pi22) + (ys21_1*xo1u) * (1 + pi11) + (ys21_1*xo1d) * (1 + pi31),
pi22 == (ys22_1*xo1l) * (1 + pi21) + (ys22_1*xo1r) * (1 + pi23) + (ys22_1*xo1u) * (1 + pi12) + (ys22_1*xo1d) * (1 + pi32),
pi23 == (ys23_1*xo1l) * (1 + pi22) + (ys23_1*xo1r) * (1 + pi24) + (ys23_1*xo1u) * (1 + pi13) + (ys23_1*xo1d) * (1 + pi33),
pi24 == (ys24_1*xo1l) * (1 + pi23) + (ys24_1*xo1r) * (1 + pi25) + (ys24_1*xo1u) * (1 + pi14) + (ys24_1*xo1d) * (1 + pi34),
pi25 == (ys25_1*xo1l) * (1 + pi24) + (ys25_1*xo1r) * (1 + pi26) + (ys25_1*xo1u) * (1 + pi15) + (ys25_1*xo1d) * (1 + pi35),
pi26 == (ys26_1*xo1l) * (1 + pi25) + (ys26_1*xo1r) * (1 + pi27) + (ys26_1*xo1u) * (1 + pi16) + (ys26_1*xo1d) * (1 + pi36),
pi27 == (ys27_1*xo1l) * (1 + pi26) + (ys27_1*xo1r) * (1 + pi28) + (ys27_1*xo1u) * (1 + pi17) + (ys27_1*xo1d) * (1 + pi37),
pi28 == (ys28_1*xo1l) * (1 + pi27) + (ys28_1*xo1r) * (1 + pi29) + (ys28_1*xo1u) * (1 + pi18) + (ys28_1*xo1d) * (1 + pi38),
pi29 == (ys29_1*xo1l) * (1 + pi28) + (ys29_1*xo1r) * (1 + pi29) + (ys29_1*xo1u) * (1 + pi19) + (ys29_1*xo1d) * (1 + pi39),
pi30 == (ys30_1*xo1l) * (1 + pi30) + (ys30_1*xo1r) * (1 + pi31) + (ys30_1*xo1u) * (1 + pi20) + (ys30_1*xo1d) * (1 + pi40),
pi31 == (ys31_1*xo1l) * (1 + pi30) + (ys31_1*xo1r) * (1 + pi32) + (ys31_1*xo1u) * (1 + pi21) + (ys31_1*xo1d) * (1 + pi41),
pi32 == (ys32_1*xo1l) * (1 + pi31) + (ys32_1*xo1r) * (1 + pi33) + (ys32_1*xo1u) * (1 + pi22) + (ys32_1*xo1d) * (1 + pi42),
pi33 == (ys33_1*xo1l) * (1 + pi32) + (ys33_1*xo1r) * (1 + pi34) + (ys33_1*xo1u) * (1 + pi23) + (ys33_1*xo1d) * (1 + pi43),
pi34 == (ys34_1*xo1l) * (1 + pi33) + (ys34_1*xo1r) * (1 + pi35) + (ys34_1*xo1u) * (1 + pi24) + (ys34_1*xo1d) * (1 + pi44),
pi35 == (ys35_1*xo1l) * (1 + pi34) + (ys35_1*xo1r) * (1 + pi36) + (ys35_1*xo1u) * (1 + pi25) + (ys35_1*xo1d) * (1 + pi45),
pi36 == (ys36_1*xo1l) * (1 + pi35) + (ys36_1*xo1r) * (1 + pi37) + (ys36_1*xo1u) * (1 + pi26) + (ys36_1*xo1d) * (1 + pi46),
pi37 == (ys37_1*xo1l) * (1 + pi36) + (ys37_1*xo1r) * (1 + pi38) + (ys37_1*xo1u) * (1 + pi27) + (ys37_1*xo1d) * (1 + pi47),
pi38 == (ys38_1*xo1l) * (1 + pi37) + (ys38_1*xo1r) * (1 + pi39) + (ys38_1*xo1u) * (1 + pi28) + (ys38_1*xo1d) * (1 + pi48),
pi39 == (ys39_1*xo1l) * (1 + pi38) + (ys39_1*xo1r) * (1 + pi39) + (ys39_1*xo1u) * (1 + pi29) + (ys39_1*xo1d) * (1 + pi49),
pi40 == (ys40_1*xo1l) * (1 + pi40) + (ys40_1*xo1r) * (1 + pi41) + (ys40_1*xo1u) * (1 + pi30) + (ys40_1*xo1d) * (1 + pi50),
pi41 == (ys41_1*xo1l) * (1 + pi40) + (ys41_1*xo1r) * (1 + pi42) + (ys41_1*xo1u) * (1 + pi31) + (ys41_1*xo1d) * (1 + pi51),
pi42 == (ys42_1*xo1l) * (1 + pi41) + (ys42_1*xo1r) * (1 + pi43) + (ys42_1*xo1u) * (1 + pi32) + (ys42_1*xo1d) * (1 + pi52),
pi43 == (ys43_1*xo1l) * (1 + pi42) + (ys43_1*xo1r) * (1 + pi44) + (ys43_1*xo1u) * (1 + pi33) + (ys43_1*xo1d) * (1 + pi53),
pi44 == (ys44_1*xo1l) * (1 + pi43) + (ys44_1*xo1r) * (1 + pi45) + (ys44_1*xo1u) * (1 + pi34) + (ys44_1*xo1d) * (1 + pi54),
pi45 == (ys45_1*xo1l) * (1 + pi44) + (ys45_1*xo1r) * (1 + pi46) + (ys45_1*xo1u) * (1 + pi35) + (ys45_1*xo1d) * (1 + pi55),
pi46 == (ys46_1*xo1l) * (1 + pi45) + (ys46_1*xo1r) * (1 + pi47) + (ys46_1*xo1u) * (1 + pi36) + (ys46_1*xo1d) * (1 + pi56),
pi47 == (ys47_1*xo1l) * (1 + pi46) + (ys47_1*xo1r) * (1 + pi48) + (ys47_1*xo1u) * (1 + pi37) + (ys47_1*xo1d) * (1 + pi57),
pi48 == (ys48_1*xo1l) * (1 + pi47) + (ys48_1*xo1r) * (1 + pi49) + (ys48_1*xo1u) * (1 + pi38) + (ys48_1*xo1d) * (1 + pi58),
pi49 == (ys49_1*xo1l) * (1 + pi48) + (ys49_1*xo1r) * (1 + pi49) + (ys49_1*xo1u) * (1 + pi39) + (ys49_1*xo1d) * (1 + pi59),
pi50 == (ys50_1*xo1l) * (1 + pi50) + (ys50_1*xo1r) * (1 + pi51) + (ys50_1*xo1u) * (1 + pi40) + (ys50_1*xo1d) * (1 + pi60),
pi51 == (ys51_1*xo1l) * (1 + pi50) + (ys51_1*xo1r) * (1 + pi52) + (ys51_1*xo1u) * (1 + pi41) + (ys51_1*xo1d) * (1 + pi61),
pi52 == (ys52_1*xo1l) * (1 + pi51) + (ys52_1*xo1r) * (1 + pi53) + (ys52_1*xo1u) * (1 + pi42) + (ys52_1*xo1d) * (1 + pi62),
pi53 == (ys53_1*xo1l) * (1 + pi52) + (ys53_1*xo1r) * (1 + pi54) + (ys53_1*xo1u) * (1 + pi43) + (ys53_1*xo1d) * (1 + pi63),
pi54 == (ys54_1*xo1l) * (1 + pi53) + (ys54_1*xo1r) * (1 + pi55) + (ys54_1*xo1u) * (1 + pi44) + (ys54_1*xo1d) * (1 + pi64),
pi55 == (ys55_1*xo1l) * (1 + pi54) + (ys55_1*xo1r) * (1 + pi56) + (ys55_1*xo1u) * (1 + pi45) + (ys55_1*xo1d) * (1 + pi65),
pi56 == (ys56_1*xo1l) * (1 + pi55) + (ys56_1*xo1r) * (1 + pi57) + (ys56_1*xo1u) * (1 + pi46) + (ys56_1*xo1d) * (1 + pi66),
pi57 == (ys57_1*xo1l) * (1 + pi56) + (ys57_1*xo1r) * (1 + pi58) + (ys57_1*xo1u) * (1 + pi47) + (ys57_1*xo1d) * (1 + pi67),
pi58 == (ys58_1*xo1l) * (1 + pi57) + (ys58_1*xo1r) * (1 + pi59) + (ys58_1*xo1u) * (1 + pi48) + (ys58_1*xo1d) * (1 + pi68),
pi59 == (ys59_1*xo1l) * (1 + pi58) + (ys59_1*xo1r) * (1 + pi59) + (ys59_1*xo1u) * (1 + pi49) + (ys59_1*xo1d) * (1 + pi69),
pi60 == (ys60_1*xo1l) * (1 + pi60) + (ys60_1*xo1r) * (1 + pi61) + (ys60_1*xo1u) * (1 + pi50) + (ys60_1*xo1d) * (1 + pi70),
pi61 == (ys61_1*xo1l) * (1 + pi60) + (ys61_1*xo1r) * (1 + pi62) + (ys61_1*xo1u) * (1 + pi51) + (ys61_1*xo1d) * (1 + pi71),
pi62 == (ys62_1*xo1l) * (1 + pi61) + (ys62_1*xo1r) * (1 + pi63) + (ys62_1*xo1u) * (1 + pi52) + (ys62_1*xo1d) * (1 + pi72),
pi63 == (ys63_1*xo1l) * (1 + pi62) + (ys63_1*xo1r) * (1 + pi64) + (ys63_1*xo1u) * (1 + pi53) + (ys63_1*xo1d) * (1 + pi73),
pi64 == (ys64_1*xo1l) * (1 + pi63) + (ys64_1*xo1r) * (1 + pi65) + (ys64_1*xo1u) * (1 + pi54) + (ys64_1*xo1d) * (1 + pi74),
pi65 == (ys65_1*xo1l) * (1 + pi64) + (ys65_1*xo1r) * (1 + pi66) + (ys65_1*xo1u) * (1 + pi55) + (ys65_1*xo1d) * (1 + pi75),
pi66 == (ys66_1*xo1l) * (1 + pi65) + (ys66_1*xo1r) * (1 + pi67) + (ys66_1*xo1u) * (1 + pi56) + (ys66_1*xo1d) * (1 + pi76),
pi67 == (ys67_1*xo1l) * (1 + pi66) + (ys67_1*xo1r) * (1 + pi68) + (ys67_1*xo1u) * (1 + pi57) + (ys67_1*xo1d) * (1 + pi77),
pi68 == (ys68_1*xo1l) * (1 + pi67) + (ys68_1*xo1r) * (1 + pi69) + (ys68_1*xo1u) * (1 + pi58) + (ys68_1*xo1d) * (1 + pi78),
pi69 == (ys69_1*xo1l) * (1 + pi68) + (ys69_1*xo1r) * (1 + pi69) + (ys69_1*xo1u) * (1 + pi59) + (ys69_1*xo1d) * (1 + pi79),
pi70 == (ys70_1*xo1l) * (1 + pi70) + (ys70_1*xo1r) * (1 + pi71) + (ys70_1*xo1u) * (1 + pi60) + (ys70_1*xo1d) * (1 + pi80),
pi71 == (ys71_1*xo1l) * (1 + pi70) + (ys71_1*xo1r) * (1 + pi72) + (ys71_1*xo1u) * (1 + pi61) + (ys71_1*xo1d) * (1 + pi81),
pi72 == (ys72_1*xo1l) * (1 + pi71) + (ys72_1*xo1r) * (1 + pi73) + (ys72_1*xo1u) * (1 + pi62) + (ys72_1*xo1d) * (1 + pi82),
pi73 == (ys73_1*xo1l) * (1 + pi72) + (ys73_1*xo1r) * (1 + pi74) + (ys73_1*xo1u) * (1 + pi63) + (ys73_1*xo1d) * (1 + pi83),
pi74 == (ys74_1*xo1l) * (1 + pi73) + (ys74_1*xo1r) * (1 + pi75) + (ys74_1*xo1u) * (1 + pi64) + (ys74_1*xo1d) * (1 + pi84),
pi75 == (ys75_1*xo1l) * (1 + pi74) + (ys75_1*xo1r) * (1 + pi76) + (ys75_1*xo1u) * (1 + pi65) + (ys75_1*xo1d) * (1 + pi85),
pi76 == (ys76_1*xo1l) * (1 + pi75) + (ys76_1*xo1r) * (1 + pi77) + (ys76_1*xo1u) * (1 + pi66) + (ys76_1*xo1d) * (1 + pi86),
pi77 == (ys77_1*xo1l) * (1 + pi76) + (ys77_1*xo1r) * (1 + pi78) + (ys77_1*xo1u) * (1 + pi67) + (ys77_1*xo1d) * (1 + pi87),
pi78 == (ys78_1*xo1l) * (1 + pi77) + (ys78_1*xo1r) * (1 + pi79) + (ys78_1*xo1u) * (1 + pi68) + (ys78_1*xo1d) * (1 + pi88),
pi79 == (ys79_1*xo1l) * (1 + pi78) + (ys79_1*xo1r) * (1 + pi79) + (ys79_1*xo1u) * (1 + pi69) + (ys79_1*xo1d) * (1 + pi89),
pi80 == (ys80_1*xo1l) * (1 + pi80) + (ys80_1*xo1r) * (1 + pi81) + (ys80_1*xo1u) * (1 + pi70) + (ys80_1*xo1d) * (1 + pi90),
pi81 == (ys81_1*xo1l) * (1 + pi80) + (ys81_1*xo1r) * (1 + pi82) + (ys81_1*xo1u) * (1 + pi71) + (ys81_1*xo1d) * (1 + pi91),
pi82 == (ys82_1*xo1l) * (1 + pi81) + (ys82_1*xo1r) * (1 + pi83) + (ys82_1*xo1u) * (1 + pi72) + (ys82_1*xo1d) * (1 + pi92),
pi83 == (ys83_1*xo1l) * (1 + pi82) + (ys83_1*xo1r) * (1 + pi84) + (ys83_1*xo1u) * (1 + pi73) + (ys83_1*xo1d) * (1 + pi93),
pi84 == (ys84_1*xo1l) * (1 + pi83) + (ys84_1*xo1r) * (1 + pi85) + (ys84_1*xo1u) * (1 + pi74) + (ys84_1*xo1d) * (1 + pi94),
pi85 == (ys85_1*xo1l) * (1 + pi84) + (ys85_1*xo1r) * (1 + pi86) + (ys85_1*xo1u) * (1 + pi75) + (ys85_1*xo1d) * (1 + pi95),
pi86 == (ys86_1*xo1l) * (1 + pi85) + (ys86_1*xo1r) * (1 + pi87) + (ys86_1*xo1u) * (1 + pi76) + (ys86_1*xo1d) * (1 + pi96),
pi87 == (ys87_1*xo1l) * (1 + pi86) + (ys87_1*xo1r) * (1 + pi88) + (ys87_1*xo1u) * (1 + pi77) + (ys87_1*xo1d) * (1 + pi97),
pi88 == (ys88_1*xo1l) * (1 + pi87) + (ys88_1*xo1r) * (1 + pi89) + (ys88_1*xo1u) * (1 + pi78) + (ys88_1*xo1d) * (1 + pi98),
pi89 == (ys89_1*xo1l) * (1 + pi88) + (ys89_1*xo1r) * (1 + pi89) + (ys89_1*xo1u) * (1 + pi79) + (ys89_1*xo1d) * (1 + pi99),
pi90 == (ys90_1*xo1l) * (1 + pi90) + (ys90_1*xo1r) * (1 + pi91) + (ys90_1*xo1u) * (1 + pi80) + (ys90_1*xo1d) * (1 + pi90),
pi91 == (ys91_1*xo1l) * (1 + pi90) + (ys91_1*xo1r) * (1 + pi92) + (ys91_1*xo1u) * (1 + pi81) + (ys91_1*xo1d) * (1 + pi91),
pi92 == (ys92_1*xo1l) * (1 + pi91) + (ys92_1*xo1r) * (1 + pi93) + (ys92_1*xo1u) * (1 + pi82) + (ys92_1*xo1d) * (1 + pi92),
pi93 == (ys93_1*xo1l) * (1 + pi92) + (ys93_1*xo1r) * (1 + pi94) + (ys93_1*xo1u) * (1 + pi83) + (ys93_1*xo1d) * (1 + pi93),
pi94 == (ys94_1*xo1l) * (1 + pi93) + (ys94_1*xo1r) * (1 + pi95) + (ys94_1*xo1u) * (1 + pi84) + (ys94_1*xo1d) * (1 + pi94),
pi95 == 0, 
pi96 == (ys96_1*xo1l) * (1 + pi95) + (ys96_1*xo1r) * (1 + pi97) + (ys96_1*xo1u) * (1 + pi86) + (ys96_1*xo1d) * (1 + pi96),
pi97 == (ys97_1*xo1l) * (1 + pi96) + (ys97_1*xo1r) * (1 + pi98) + (ys97_1*xo1u) * (1 + pi87) + (ys97_1*xo1d) * (1 + pi97),
pi98 == (ys98_1*xo1l) * (1 + pi97) + (ys98_1*xo1r) * (1 + pi99) + (ys98_1*xo1u) * (1 + pi88) + (ys98_1*xo1d) * (1 + pi98),
pi99 == (ys99_1*xo1l) * (1 + pi98) + (ys99_1*xo1r) * (1 + pi99) + (ys99_1*xo1u) * (1 + pi89) + (ys99_1*xo1d) * (1 + pi99),
exp==((pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi30+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47+pi48+pi49+pi50+pi51+pi52+pi53+pi54+pi55+pi56+pi57+pi58+pi59+pi60+pi61+pi62+pi63+pi64+pi65+pi66+pi67+pi68+pi69+pi70+pi71+pi72+pi73+pi74+pi75+pi76+pi77+pi78+pi79+pi80+pi81+pi82+pi83+pi84+pi85+pi86+pi87+pi88+pi89+pi90+pi91+pi92+pi93+pi94+pi96+pi97+pi98+pi99)) * Q(1,99),
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
xo1r== Q(26, 99),
xo1d== Q(16, 33),
xo1l== Q(25, 99),
xo1u + xo1r + xo1d + xo1l == 1,
# Assigned observables
ys40_1 == 1,
ys49_1 == 1,
ys51_1 == 1,
ys80_1 == 1,
ys89_1 == 1,
ys98_1 == 1,
ys5_1 == 1,
ys22_1 == 1,
ys62_1 == 1,
ys71_1 == 1,
ys42_1 == 1,
ys36_1 == 1,
ys53_1 == 1,
ys82_1 == 1,
ys91_1 == 1,
ys7_1 == 1,
ys24_1 == 1,
ys18_1 == 1,
ys64_1 == 1,
ys73_1 == 1,
ys38_1 == 1,
ys55_1 == 1,
ys84_1 == 1,
ys93_1 == 1,
ys0_1 == 1,
ys9_1 == 1,
ys66_1 == 1,
ys75_1 == 1,
ys31_1 == 1,
ys57_1 == 1,
ys2_1 == 1,
ys13_1 == 1,
ys77_1 == 1,
ys33_1 == 1,
ys50_1 == 1,
ys59_1 == 1,
ys97_1 == 1,
ys15_1 == 1,
ys61_1 == 1,
ys70_1 == 1,
ys79_1 == 1,
ys35_1 == 1,
ys52_1 == 1,
ys44_1 == 1,
ys90_1 == 1,
ys99_1 == 1,
ys17_1 == 1,
ys26_1 == 1,
ys72_1 == 1,
ys37_1 == 1,
ys54_1 == 1,
ys46_1 == 1,
ys92_1 == 1,
ys86_1 == 1,
ys10_1 == 1,
ys19_1 == 1,
ys28_1 == 1,
ys74_1 == 1,
ys68_1 == 1,
ys30_1 == 1,
ys39_1 == 1,
ys56_1 == 1,
ys48_1 == 1,
ys88_1 == 1,
ys12_1 == 1,
ys4_1 == 1,
ys21_1 == 1,
ys32_1 == 1,
ys41_1 == 1,
ys81_1 == 1,
ys14_1 == 1,
ys6_1 == 1,
ys23_1 == 1,
ys63_1 == 1,
ys34_1 == 1,
ys43_1 == 1,
ys83_1 == 1,
ys16_1 == 1,
ys8_1 == 1,
ys25_1 == 1,
ys65_1 == 1,
ys45_1 == 1,
ys85_1 == 1,
ys94_1 == 1,
ys1_1 == 1,
ys27_1 == 1,
ys67_1 == 1,
ys76_1 == 1,
ys47_1 == 1,
ys58_1 == 1,
ys87_1 == 1,
ys11_1 == 1,
ys3_1 == 1,
ys20_1 == 1,
ys96_1 == 1,
ys29_1 == 1,
ys60_1 == 1,
ys69_1 == 1,
ys78_1 == 1,
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
ys21_1 == 1,
ys22_1 == 1,
ys23_1 == 1,
ys24_1 == 1,
ys25_1 == 1,
ys26_1 == 1,
ys27_1 == 1,
ys28_1 == 1,
ys29_1 == 1,
ys30_1 == 1,
ys31_1 == 1,
ys32_1 == 1,
ys33_1 == 1,
ys34_1 == 1,
ys35_1 == 1,
ys36_1 == 1,
ys37_1 == 1,
ys38_1 == 1,
ys39_1 == 1,
ys40_1 == 1,
ys41_1 == 1,
ys42_1 == 1,
ys43_1 == 1,
ys44_1 == 1,
ys45_1 == 1,
ys46_1 == 1,
ys47_1 == 1,
ys48_1 == 1,
ys49_1 == 1,
ys50_1 == 1,
ys51_1 == 1,
ys52_1 == 1,
ys53_1 == 1,
ys54_1 == 1,
ys55_1 == 1,
ys56_1 == 1,
ys57_1 == 1,
ys58_1 == 1,
ys59_1 == 1,
ys60_1 == 1,
ys61_1 == 1,
ys62_1 == 1,
ys63_1 == 1,
ys64_1 == 1,
ys65_1 == 1,
ys66_1 == 1,
ys67_1 == 1,
ys68_1 == 1,
ys69_1 == 1,
ys70_1 == 1,
ys71_1 == 1,
ys72_1 == 1,
ys73_1 == 1,
ys74_1 == 1,
ys75_1 == 1,
ys76_1 == 1,
ys77_1 == 1,
ys78_1 == 1,
ys79_1 == 1,
ys80_1 == 1,
ys81_1 == 1,
ys82_1 == 1,
ys83_1 == 1,
ys84_1 == 1,
ys85_1 == 1,
ys86_1 == 1,
ys87_1 == 1,
ys88_1 == 1,
ys89_1 == 1,
ys90_1 == 1,
ys91_1 == 1,
ys92_1 == 1,
ys93_1 == 1,
ys94_1 == 1,
ys96_1 == 1,
ys97_1 == 1,
ys98_1 == 1,
ys99_1 == 1
)


sol = lambda : solver.model() if solver.check() == sat else "No Solution" if solver.check() == unsat else None
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
pi100 = Real('pi100')
pi101 = Real('pi101')
pi102 = Real('pi102')
pi103 = Real('pi103')
pi104 = Real('pi104')
pi105 = Real('pi105')
pi106 = Real('pi106')
pi107 = Real('pi107')
pi108 = Real('pi108')
pi109 = Real('pi109')
pi110 = Real('pi110')
pi111 = Real('pi111')
pi112 = Real('pi112')
pi113 = Real('pi113')
pi114 = Real('pi114')
pi115 = Real('pi115')
pi116 = Real('pi116')
pi117 = Real('pi117')
pi118 = Real('pi118')
pi119 = Real('pi119')
pi120 = Real('pi120')
pi121 = Real('pi121')
pi122 = Real('pi122')
pi123 = Real('pi123')
pi124 = Real('pi124')
pi125 = Real('pi125')
pi126 = Real('pi126')
pi127 = Real('pi127')
pi128 = Real('pi128')
pi129 = Real('pi129')
pi130 = Real('pi130')
pi131 = Real('pi131')
pi132 = Real('pi132')
pi133 = Real('pi133')
pi134 = Real('pi134')
pi135 = Real('pi135')
pi136 = Real('pi136')
pi137 = Real('pi137')
pi138 = Real('pi138')
pi139 = Real('pi139')
pi140 = Real('pi140')
pi141 = Real('pi141')
pi142 = Real('pi142')
pi143 = Real('pi143')
pi144 = Real('pi144')
pi145 = Real('pi145')
pi146 = Real('pi146')
pi147 = Real('pi147')
pi148 = Real('pi148')
pi149 = Real('pi149')
pi150 = Real('pi150')
pi151 = Real('pi151')
pi152 = Real('pi152')
pi153 = Real('pi153')
pi154 = Real('pi154')
pi155 = Real('pi155')
pi156 = Real('pi156')
pi157 = Real('pi157')
pi158 = Real('pi158')
pi159 = Real('pi159')
pi160 = Real('pi160')
pi161 = Real('pi161')
pi162 = Real('pi162')
pi163 = Real('pi163')
pi164 = Real('pi164')
pi165 = Real('pi165')
pi166 = Real('pi166')
pi167 = Real('pi167')
pi168 = Real('pi168')
pi169 = Real('pi169')
pi170 = Real('pi170')
pi171 = Real('pi171')
pi172 = Real('pi172')
pi173 = Real('pi173')
pi174 = Real('pi174')
pi175 = Real('pi175')
pi176 = Real('pi176')
pi177 = Real('pi177')
pi178 = Real('pi178')
pi179 = Real('pi179')
pi180 = Real('pi180')
pi181 = Real('pi181')
pi182 = Real('pi182')
pi183 = Real('pi183')
pi184 = Real('pi184')
pi185 = Real('pi185')
pi186 = Real('pi186')
pi187 = Real('pi187')
pi188 = Real('pi188')
pi189 = Real('pi189')
pi190 = Real('pi190')
pi191 = Real('pi191')
pi192 = Real('pi192')
pi193 = Real('pi193')
pi194 = Real('pi194')
pi195 = Real('pi195')

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
ys100_1 = Real('ys100_1')
ys101_1 = Real('ys101_1')
ys102_1 = Real('ys102_1')
ys103_1 = Real('ys103_1')
ys104_1 = Real('ys104_1')
ys105_1 = Real('ys105_1')
ys106_1 = Real('ys106_1')
ys107_1 = Real('ys107_1')
ys108_1 = Real('ys108_1')
ys109_1 = Real('ys109_1')
ys110_1 = Real('ys110_1')
ys111_1 = Real('ys111_1')
ys112_1 = Real('ys112_1')
ys113_1 = Real('ys113_1')
ys114_1 = Real('ys114_1')
ys115_1 = Real('ys115_1')
ys116_1 = Real('ys116_1')
ys117_1 = Real('ys117_1')
ys118_1 = Real('ys118_1')
ys119_1 = Real('ys119_1')
ys120_1 = Real('ys120_1')
ys121_1 = Real('ys121_1')
ys122_1 = Real('ys122_1')
ys123_1 = Real('ys123_1')
ys124_1 = Real('ys124_1')
ys125_1 = Real('ys125_1')
ys126_1 = Real('ys126_1')
ys127_1 = Real('ys127_1')
ys128_1 = Real('ys128_1')
ys129_1 = Real('ys129_1')
ys130_1 = Real('ys130_1')
ys131_1 = Real('ys131_1')
ys132_1 = Real('ys132_1')
ys133_1 = Real('ys133_1')
ys134_1 = Real('ys134_1')
ys135_1 = Real('ys135_1')
ys136_1 = Real('ys136_1')
ys137_1 = Real('ys137_1')
ys138_1 = Real('ys138_1')
ys139_1 = Real('ys139_1')
ys140_1 = Real('ys140_1')
ys141_1 = Real('ys141_1')
ys142_1 = Real('ys142_1')
ys143_1 = Real('ys143_1')
ys144_1 = Real('ys144_1')
ys145_1 = Real('ys145_1')
ys146_1 = Real('ys146_1')
ys147_1 = Real('ys147_1')
ys148_1 = Real('ys148_1')
ys149_1 = Real('ys149_1')
ys150_1 = Real('ys150_1')
ys151_1 = Real('ys151_1')
ys152_1 = Real('ys152_1')
ys153_1 = Real('ys153_1')
ys154_1 = Real('ys154_1')
ys155_1 = Real('ys155_1')
ys156_1 = Real('ys156_1')
ys157_1 = Real('ys157_1')
ys158_1 = Real('ys158_1')
ys159_1 = Real('ys159_1')
ys160_1 = Real('ys160_1')
ys161_1 = Real('ys161_1')
ys162_1 = Real('ys162_1')
ys163_1 = Real('ys163_1')
ys164_1 = Real('ys164_1')
ys165_1 = Real('ys165_1')
ys166_1 = Real('ys166_1')
ys167_1 = Real('ys167_1')
ys168_1 = Real('ys168_1')
ys169_1 = Real('ys169_1')
ys170_1 = Real('ys170_1')
ys171_1 = Real('ys171_1')
ys172_1 = Real('ys172_1')
ys173_1 = Real('ys173_1')
ys174_1 = Real('ys174_1')
ys175_1 = Real('ys175_1')
ys176_1 = Real('ys176_1')
ys177_1 = Real('ys177_1')
ys178_1 = Real('ys178_1')
ys179_1 = Real('ys179_1')
ys180_1 = Real('ys180_1')
ys181_1 = Real('ys181_1')
ys182_1 = Real('ys182_1')
ys183_1 = Real('ys183_1')
ys184_1 = Real('ys184_1')
ys185_1 = Real('ys185_1')
ys186_1 = Real('ys186_1')
ys187_1 = Real('ys187_1')
ys188_1 = Real('ys188_1')
ys189_1 = Real('ys189_1')
ys190_1 = Real('ys190_1')
ys191_1 = Real('ys191_1')
ys192_1 = Real('ys192_1')
ys193_1 = Real('ys193_1')
ys194_1 = Real('ys194_1')
ys195_1 = Real('ys195_1')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo1u = Real('xo1u')
xo1d = Real('xo1d')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=14, pi1>=13, pi2>=13, pi3>=14, pi4>=15, pi5>=16, pi6>=17, pi7>=18, pi8>=19, pi9>=20, pi10>=21, pi11>=22, pi12>=23, pi13>=24, pi14>=13, pi15>=12, pi16>=12, pi17>=13, pi18>=14, pi19>=15, pi20>=16, pi21>=17, pi22>=18, pi23>=19, pi24>=20, pi25>=21, pi26>=22, pi27>=23, pi28>=12, pi29>=11, pi30>=11, pi31>=12, pi32>=13, pi33>=14, pi34>=15, pi35>=16, pi36>=17, pi37>=18, pi38>=19, pi39>=20, pi40>=21, pi41>=22, pi42>=11, pi43>=10, pi44>=10, pi45>=11, pi46>=12, pi47>=13, pi48>=14, pi49>=15, pi50>=16, pi51>=17, pi52>=18, pi53>=19, pi54>=20, pi55>=21, pi56>=10, pi57>=9, pi58>=9, pi59>=10, pi60>=11, pi61>=12, pi62>=13, pi63>=14, pi64>=15, pi65>=16, pi66>=17, pi67>=18, pi68>=19, pi69>=20, pi70>=9, pi71>=8, pi72>=8, pi73>=9, pi74>=10, pi75>=11, pi76>=12, pi77>=13, pi78>=14, pi79>=15, pi80>=16, pi81>=17, pi82>=18, pi83>=19, pi84>=8, pi85>=7, pi86>=7, pi87>=8, pi88>=9, pi89>=10, pi90>=11, pi91>=12, pi92>=13, pi93>=14, pi94>=15, pi95>=16, pi96>=17, pi97>=18, pi98>=7, pi99>=6, pi100>=6, pi101>=7, pi102>=8, pi103>=9, pi104>=10, pi105>=11, pi106>=12, pi107>=13, pi108>=14, pi109>=15, pi110>=16, pi111>=17, pi112>=6, pi113>=5, pi114>=5, pi115>=6, pi116>=7, pi117>=8, pi118>=9, pi119>=10, pi120>=11, pi121>=12, pi122>=13, pi123>=14, pi124>=15, pi125>=16, pi126>=5, pi127>=4, pi128>=4, pi129>=5, pi130>=6, pi131>=7, pi132>=8, pi133>=9, pi134>=10, pi135>=11, pi136>=12, pi137>=13, pi138>=14, pi139>=15, pi140>=4, pi141>=3, pi142>=3, pi143>=4, pi144>=5, pi145>=6, pi146>=7, pi147>=8, pi148>=9, pi149>=10, pi150>=11, pi151>=12, pi152>=13, pi153>=14, pi154>=3, pi155>=2, pi156>=2, pi157>=3, pi158>=4, pi159>=5, pi160>=6, pi161>=7, pi162>=8, pi163>=9, pi164>=10, pi165>=11, pi166>=12, pi167>=13, pi168>=2, pi169>=1, pi170>=1, pi171>=2, pi172>=3, pi173>=4, pi174>=5, pi175>=6, pi176>=7, pi177>=8, pi178>=9, pi179>=10, pi180>=11, pi181>=12, pi182>=1, pi183>=0, pi184>=0, pi185>=2, pi186>=3, pi187>=4, pi188>=5, pi189>=6, pi190>=7, pi191>=8, pi192>=9, pi193>=10, pi194>=11, pi195>=12, 
# Expected cost/reard equations
pi0 == (ys0_1*xo1l) * (1 + pi0) + (ys0_1*xo1r) * (1 + pi1) + (ys0_1*xo1u) * (1 + pi0) + (ys0_1*xo1d) * (1 + pi14),
pi1 == (ys1_1*xo1l) * (1 + pi0) + (ys1_1*xo1r) * (1 + pi2) + (ys1_1*xo1u) * (1 + pi1) + (ys1_1*xo1d) * (1 + pi15),
pi2 == (ys2_1*xo1l) * (1 + pi1) + (ys2_1*xo1r) * (1 + pi3) + (ys2_1*xo1u) * (1 + pi2) + (ys2_1*xo1d) * (1 + pi16),
pi3 == (ys3_1*xo1l) * (1 + pi2) + (ys3_1*xo1r) * (1 + pi4) + (ys3_1*xo1u) * (1 + pi3) + (ys3_1*xo1d) * (1 + pi17),
pi4 == (ys4_1*xo1l) * (1 + pi3) + (ys4_1*xo1r) * (1 + pi5) + (ys4_1*xo1u) * (1 + pi4) + (ys4_1*xo1d) * (1 + pi18),
pi5 == (ys5_1*xo1l) * (1 + pi4) + (ys5_1*xo1r) * (1 + pi6) + (ys5_1*xo1u) * (1 + pi5) + (ys5_1*xo1d) * (1 + pi19),
pi6 == (ys6_1*xo1l) * (1 + pi5) + (ys6_1*xo1r) * (1 + pi7) + (ys6_1*xo1u) * (1 + pi6) + (ys6_1*xo1d) * (1 + pi20),
pi7 == (ys7_1*xo1l) * (1 + pi6) + (ys7_1*xo1r) * (1 + pi8) + (ys7_1*xo1u) * (1 + pi7) + (ys7_1*xo1d) * (1 + pi21),
pi8 == (ys8_1*xo1l) * (1 + pi7) + (ys8_1*xo1r) * (1 + pi9) + (ys8_1*xo1u) * (1 + pi8) + (ys8_1*xo1d) * (1 + pi22),
pi9 == (ys9_1*xo1l) * (1 + pi8) + (ys9_1*xo1r) * (1 + pi10) + (ys9_1*xo1u) * (1 + pi9) + (ys9_1*xo1d) * (1 + pi23),
pi10 == (ys10_1*xo1l) * (1 + pi9) + (ys10_1*xo1r) * (1 + pi11) + (ys10_1*xo1u) * (1 + pi10) + (ys10_1*xo1d) * (1 + pi24),
pi11 == (ys11_1*xo1l) * (1 + pi10) + (ys11_1*xo1r) * (1 + pi12) + (ys11_1*xo1u) * (1 + pi11) + (ys11_1*xo1d) * (1 + pi25),
pi12 == (ys12_1*xo1l) * (1 + pi11) + (ys12_1*xo1r) * (1 + pi13) + (ys12_1*xo1u) * (1 + pi12) + (ys12_1*xo1d) * (1 + pi26),
pi13 == (ys13_1*xo1l) * (1 + pi12) + (ys13_1*xo1r) * (1 + pi13) + (ys13_1*xo1u) * (1 + pi13) + (ys13_1*xo1d) * (1 + pi27),
pi14 == (ys14_1*xo1l) * (1 + pi14) + (ys14_1*xo1r) * (1 + pi15) + (ys14_1*xo1u) * (1 + pi0) + (ys14_1*xo1d) * (1 + pi28),
pi15 == (ys15_1*xo1l) * (1 + pi14) + (ys15_1*xo1r) * (1 + pi16) + (ys15_1*xo1u) * (1 + pi1) + (ys15_1*xo1d) * (1 + pi29),
pi16 == (ys16_1*xo1l) * (1 + pi15) + (ys16_1*xo1r) * (1 + pi17) + (ys16_1*xo1u) * (1 + pi2) + (ys16_1*xo1d) * (1 + pi30),
pi17 == (ys17_1*xo1l) * (1 + pi16) + (ys17_1*xo1r) * (1 + pi18) + (ys17_1*xo1u) * (1 + pi3) + (ys17_1*xo1d) * (1 + pi31),
pi18 == (ys18_1*xo1l) * (1 + pi17) + (ys18_1*xo1r) * (1 + pi19) + (ys18_1*xo1u) * (1 + pi4) + (ys18_1*xo1d) * (1 + pi32),
pi19 == (ys19_1*xo1l) * (1 + pi18) + (ys19_1*xo1r) * (1 + pi20) + (ys19_1*xo1u) * (1 + pi5) + (ys19_1*xo1d) * (1 + pi33),
pi20 == (ys20_1*xo1l) * (1 + pi19) + (ys20_1*xo1r) * (1 + pi21) + (ys20_1*xo1u) * (1 + pi6) + (ys20_1*xo1d) * (1 + pi34),
pi21 == (ys21_1*xo1l) * (1 + pi20) + (ys21_1*xo1r) * (1 + pi22) + (ys21_1*xo1u) * (1 + pi7) + (ys21_1*xo1d) * (1 + pi35),
pi22 == (ys22_1*xo1l) * (1 + pi21) + (ys22_1*xo1r) * (1 + pi23) + (ys22_1*xo1u) * (1 + pi8) + (ys22_1*xo1d) * (1 + pi36),
pi23 == (ys23_1*xo1l) * (1 + pi22) + (ys23_1*xo1r) * (1 + pi24) + (ys23_1*xo1u) * (1 + pi9) + (ys23_1*xo1d) * (1 + pi37),
pi24 == (ys24_1*xo1l) * (1 + pi23) + (ys24_1*xo1r) * (1 + pi25) + (ys24_1*xo1u) * (1 + pi10) + (ys24_1*xo1d) * (1 + pi38),
pi25 == (ys25_1*xo1l) * (1 + pi24) + (ys25_1*xo1r) * (1 + pi26) + (ys25_1*xo1u) * (1 + pi11) + (ys25_1*xo1d) * (1 + pi39),
pi26 == (ys26_1*xo1l) * (1 + pi25) + (ys26_1*xo1r) * (1 + pi27) + (ys26_1*xo1u) * (1 + pi12) + (ys26_1*xo1d) * (1 + pi40),
pi27 == (ys27_1*xo1l) * (1 + pi26) + (ys27_1*xo1r) * (1 + pi27) + (ys27_1*xo1u) * (1 + pi13) + (ys27_1*xo1d) * (1 + pi41),
pi28 == (ys28_1*xo1l) * (1 + pi28) + (ys28_1*xo1r) * (1 + pi29) + (ys28_1*xo1u) * (1 + pi14) + (ys28_1*xo1d) * (1 + pi42),
pi29 == (ys29_1*xo1l) * (1 + pi28) + (ys29_1*xo1r) * (1 + pi30) + (ys29_1*xo1u) * (1 + pi15) + (ys29_1*xo1d) * (1 + pi43),
pi30 == (ys30_1*xo1l) * (1 + pi29) + (ys30_1*xo1r) * (1 + pi31) + (ys30_1*xo1u) * (1 + pi16) + (ys30_1*xo1d) * (1 + pi44),
pi31 == (ys31_1*xo1l) * (1 + pi30) + (ys31_1*xo1r) * (1 + pi32) + (ys31_1*xo1u) * (1 + pi17) + (ys31_1*xo1d) * (1 + pi45),
pi32 == (ys32_1*xo1l) * (1 + pi31) + (ys32_1*xo1r) * (1 + pi33) + (ys32_1*xo1u) * (1 + pi18) + (ys32_1*xo1d) * (1 + pi46),
pi33 == (ys33_1*xo1l) * (1 + pi32) + (ys33_1*xo1r) * (1 + pi34) + (ys33_1*xo1u) * (1 + pi19) + (ys33_1*xo1d) * (1 + pi47),
pi34 == (ys34_1*xo1l) * (1 + pi33) + (ys34_1*xo1r) * (1 + pi35) + (ys34_1*xo1u) * (1 + pi20) + (ys34_1*xo1d) * (1 + pi48),
pi35 == (ys35_1*xo1l) * (1 + pi34) + (ys35_1*xo1r) * (1 + pi36) + (ys35_1*xo1u) * (1 + pi21) + (ys35_1*xo1d) * (1 + pi49),
pi36 == (ys36_1*xo1l) * (1 + pi35) + (ys36_1*xo1r) * (1 + pi37) + (ys36_1*xo1u) * (1 + pi22) + (ys36_1*xo1d) * (1 + pi50),
pi37 == (ys37_1*xo1l) * (1 + pi36) + (ys37_1*xo1r) * (1 + pi38) + (ys37_1*xo1u) * (1 + pi23) + (ys37_1*xo1d) * (1 + pi51),
pi38 == (ys38_1*xo1l) * (1 + pi37) + (ys38_1*xo1r) * (1 + pi39) + (ys38_1*xo1u) * (1 + pi24) + (ys38_1*xo1d) * (1 + pi52),
pi39 == (ys39_1*xo1l) * (1 + pi38) + (ys39_1*xo1r) * (1 + pi40) + (ys39_1*xo1u) * (1 + pi25) + (ys39_1*xo1d) * (1 + pi53),
pi40 == (ys40_1*xo1l) * (1 + pi39) + (ys40_1*xo1r) * (1 + pi41) + (ys40_1*xo1u) * (1 + pi26) + (ys40_1*xo1d) * (1 + pi54),
pi41 == (ys41_1*xo1l) * (1 + pi40) + (ys41_1*xo1r) * (1 + pi41) + (ys41_1*xo1u) * (1 + pi27) + (ys41_1*xo1d) * (1 + pi55),
pi42 == (ys42_1*xo1l) * (1 + pi42) + (ys42_1*xo1r) * (1 + pi43) + (ys42_1*xo1u) * (1 + pi28) + (ys42_1*xo1d) * (1 + pi56),
pi43 == (ys43_1*xo1l) * (1 + pi42) + (ys43_1*xo1r) * (1 + pi44) + (ys43_1*xo1u) * (1 + pi29) + (ys43_1*xo1d) * (1 + pi57),
pi44 == (ys44_1*xo1l) * (1 + pi43) + (ys44_1*xo1r) * (1 + pi45) + (ys44_1*xo1u) * (1 + pi30) + (ys44_1*xo1d) * (1 + pi58),
pi45 == (ys45_1*xo1l) * (1 + pi44) + (ys45_1*xo1r) * (1 + pi46) + (ys45_1*xo1u) * (1 + pi31) + (ys45_1*xo1d) * (1 + pi59),
pi46 == (ys46_1*xo1l) * (1 + pi45) + (ys46_1*xo1r) * (1 + pi47) + (ys46_1*xo1u) * (1 + pi32) + (ys46_1*xo1d) * (1 + pi60),
pi47 == (ys47_1*xo1l) * (1 + pi46) + (ys47_1*xo1r) * (1 + pi48) + (ys47_1*xo1u) * (1 + pi33) + (ys47_1*xo1d) * (1 + pi61),
pi48 == (ys48_1*xo1l) * (1 + pi47) + (ys48_1*xo1r) * (1 + pi49) + (ys48_1*xo1u) * (1 + pi34) + (ys48_1*xo1d) * (1 + pi62),
pi49 == (ys49_1*xo1l) * (1 + pi48) + (ys49_1*xo1r) * (1 + pi50) + (ys49_1*xo1u) * (1 + pi35) + (ys49_1*xo1d) * (1 + pi63),
pi50 == (ys50_1*xo1l) * (1 + pi49) + (ys50_1*xo1r) * (1 + pi51) + (ys50_1*xo1u) * (1 + pi36) + (ys50_1*xo1d) * (1 + pi64),
pi51 == (ys51_1*xo1l) * (1 + pi50) + (ys51_1*xo1r) * (1 + pi52) + (ys51_1*xo1u) * (1 + pi37) + (ys51_1*xo1d) * (1 + pi65),
pi52 == (ys52_1*xo1l) * (1 + pi51) + (ys52_1*xo1r) * (1 + pi53) + (ys52_1*xo1u) * (1 + pi38) + (ys52_1*xo1d) * (1 + pi66),
pi53 == (ys53_1*xo1l) * (1 + pi52) + (ys53_1*xo1r) * (1 + pi54) + (ys53_1*xo1u) * (1 + pi39) + (ys53_1*xo1d) * (1 + pi67),
pi54 == (ys54_1*xo1l) * (1 + pi53) + (ys54_1*xo1r) * (1 + pi55) + (ys54_1*xo1u) * (1 + pi40) + (ys54_1*xo1d) * (1 + pi68),
pi55 == (ys55_1*xo1l) * (1 + pi54) + (ys55_1*xo1r) * (1 + pi55) + (ys55_1*xo1u) * (1 + pi41) + (ys55_1*xo1d) * (1 + pi69),
pi56 == (ys56_1*xo1l) * (1 + pi56) + (ys56_1*xo1r) * (1 + pi57) + (ys56_1*xo1u) * (1 + pi42) + (ys56_1*xo1d) * (1 + pi70),
pi57 == (ys57_1*xo1l) * (1 + pi56) + (ys57_1*xo1r) * (1 + pi58) + (ys57_1*xo1u) * (1 + pi43) + (ys57_1*xo1d) * (1 + pi71),
pi58 == (ys58_1*xo1l) * (1 + pi57) + (ys58_1*xo1r) * (1 + pi59) + (ys58_1*xo1u) * (1 + pi44) + (ys58_1*xo1d) * (1 + pi72),
pi59 == (ys59_1*xo1l) * (1 + pi58) + (ys59_1*xo1r) * (1 + pi60) + (ys59_1*xo1u) * (1 + pi45) + (ys59_1*xo1d) * (1 + pi73),
pi60 == (ys60_1*xo1l) * (1 + pi59) + (ys60_1*xo1r) * (1 + pi61) + (ys60_1*xo1u) * (1 + pi46) + (ys60_1*xo1d) * (1 + pi74),
pi61 == (ys61_1*xo1l) * (1 + pi60) + (ys61_1*xo1r) * (1 + pi62) + (ys61_1*xo1u) * (1 + pi47) + (ys61_1*xo1d) * (1 + pi75),
pi62 == (ys62_1*xo1l) * (1 + pi61) + (ys62_1*xo1r) * (1 + pi63) + (ys62_1*xo1u) * (1 + pi48) + (ys62_1*xo1d) * (1 + pi76),
pi63 == (ys63_1*xo1l) * (1 + pi62) + (ys63_1*xo1r) * (1 + pi64) + (ys63_1*xo1u) * (1 + pi49) + (ys63_1*xo1d) * (1 + pi77),
pi64 == (ys64_1*xo1l) * (1 + pi63) + (ys64_1*xo1r) * (1 + pi65) + (ys64_1*xo1u) * (1 + pi50) + (ys64_1*xo1d) * (1 + pi78),
pi65 == (ys65_1*xo1l) * (1 + pi64) + (ys65_1*xo1r) * (1 + pi66) + (ys65_1*xo1u) * (1 + pi51) + (ys65_1*xo1d) * (1 + pi79),
pi66 == (ys66_1*xo1l) * (1 + pi65) + (ys66_1*xo1r) * (1 + pi67) + (ys66_1*xo1u) * (1 + pi52) + (ys66_1*xo1d) * (1 + pi80),
pi67 == (ys67_1*xo1l) * (1 + pi66) + (ys67_1*xo1r) * (1 + pi68) + (ys67_1*xo1u) * (1 + pi53) + (ys67_1*xo1d) * (1 + pi81),
pi68 == (ys68_1*xo1l) * (1 + pi67) + (ys68_1*xo1r) * (1 + pi69) + (ys68_1*xo1u) * (1 + pi54) + (ys68_1*xo1d) * (1 + pi82),
pi69 == (ys69_1*xo1l) * (1 + pi68) + (ys69_1*xo1r) * (1 + pi69) + (ys69_1*xo1u) * (1 + pi55) + (ys69_1*xo1d) * (1 + pi83),
pi70 == (ys70_1*xo1l) * (1 + pi70) + (ys70_1*xo1r) * (1 + pi71) + (ys70_1*xo1u) * (1 + pi56) + (ys70_1*xo1d) * (1 + pi84),
pi71 == (ys71_1*xo1l) * (1 + pi70) + (ys71_1*xo1r) * (1 + pi72) + (ys71_1*xo1u) * (1 + pi57) + (ys71_1*xo1d) * (1 + pi85),
pi72 == (ys72_1*xo1l) * (1 + pi71) + (ys72_1*xo1r) * (1 + pi73) + (ys72_1*xo1u) * (1 + pi58) + (ys72_1*xo1d) * (1 + pi86),
pi73 == (ys73_1*xo1l) * (1 + pi72) + (ys73_1*xo1r) * (1 + pi74) + (ys73_1*xo1u) * (1 + pi59) + (ys73_1*xo1d) * (1 + pi87),
pi74 == (ys74_1*xo1l) * (1 + pi73) + (ys74_1*xo1r) * (1 + pi75) + (ys74_1*xo1u) * (1 + pi60) + (ys74_1*xo1d) * (1 + pi88),
pi75 == (ys75_1*xo1l) * (1 + pi74) + (ys75_1*xo1r) * (1 + pi76) + (ys75_1*xo1u) * (1 + pi61) + (ys75_1*xo1d) * (1 + pi89),
pi76 == (ys76_1*xo1l) * (1 + pi75) + (ys76_1*xo1r) * (1 + pi77) + (ys76_1*xo1u) * (1 + pi62) + (ys76_1*xo1d) * (1 + pi90),
pi77 == (ys77_1*xo1l) * (1 + pi76) + (ys77_1*xo1r) * (1 + pi78) + (ys77_1*xo1u) * (1 + pi63) + (ys77_1*xo1d) * (1 + pi91),
pi78 == (ys78_1*xo1l) * (1 + pi77) + (ys78_1*xo1r) * (1 + pi79) + (ys78_1*xo1u) * (1 + pi64) + (ys78_1*xo1d) * (1 + pi92),
pi79 == (ys79_1*xo1l) * (1 + pi78) + (ys79_1*xo1r) * (1 + pi80) + (ys79_1*xo1u) * (1 + pi65) + (ys79_1*xo1d) * (1 + pi93),
pi80 == (ys80_1*xo1l) * (1 + pi79) + (ys80_1*xo1r) * (1 + pi81) + (ys80_1*xo1u) * (1 + pi66) + (ys80_1*xo1d) * (1 + pi94),
pi81 == (ys81_1*xo1l) * (1 + pi80) + (ys81_1*xo1r) * (1 + pi82) + (ys81_1*xo1u) * (1 + pi67) + (ys81_1*xo1d) * (1 + pi95),
pi82 == (ys82_1*xo1l) * (1 + pi81) + (ys82_1*xo1r) * (1 + pi83) + (ys82_1*xo1u) * (1 + pi68) + (ys82_1*xo1d) * (1 + pi96),
pi83 == (ys83_1*xo1l) * (1 + pi82) + (ys83_1*xo1r) * (1 + pi83) + (ys83_1*xo1u) * (1 + pi69) + (ys83_1*xo1d) * (1 + pi97),
pi84 == (ys84_1*xo1l) * (1 + pi84) + (ys84_1*xo1r) * (1 + pi85) + (ys84_1*xo1u) * (1 + pi70) + (ys84_1*xo1d) * (1 + pi98),
pi85 == (ys85_1*xo1l) * (1 + pi84) + (ys85_1*xo1r) * (1 + pi86) + (ys85_1*xo1u) * (1 + pi71) + (ys85_1*xo1d) * (1 + pi99),
pi86 == (ys86_1*xo1l) * (1 + pi85) + (ys86_1*xo1r) * (1 + pi87) + (ys86_1*xo1u) * (1 + pi72) + (ys86_1*xo1d) * (1 + pi100),
pi87 == (ys87_1*xo1l) * (1 + pi86) + (ys87_1*xo1r) * (1 + pi88) + (ys87_1*xo1u) * (1 + pi73) + (ys87_1*xo1d) * (1 + pi101),
pi88 == (ys88_1*xo1l) * (1 + pi87) + (ys88_1*xo1r) * (1 + pi89) + (ys88_1*xo1u) * (1 + pi74) + (ys88_1*xo1d) * (1 + pi102),
pi89 == (ys89_1*xo1l) * (1 + pi88) + (ys89_1*xo1r) * (1 + pi90) + (ys89_1*xo1u) * (1 + pi75) + (ys89_1*xo1d) * (1 + pi103),
pi90 == (ys90_1*xo1l) * (1 + pi89) + (ys90_1*xo1r) * (1 + pi91) + (ys90_1*xo1u) * (1 + pi76) + (ys90_1*xo1d) * (1 + pi104),
pi91 == (ys91_1*xo1l) * (1 + pi90) + (ys91_1*xo1r) * (1 + pi92) + (ys91_1*xo1u) * (1 + pi77) + (ys91_1*xo1d) * (1 + pi105),
pi92 == (ys92_1*xo1l) * (1 + pi91) + (ys92_1*xo1r) * (1 + pi93) + (ys92_1*xo1u) * (1 + pi78) + (ys92_1*xo1d) * (1 + pi106),
pi93 == (ys93_1*xo1l) * (1 + pi92) + (ys93_1*xo1r) * (1 + pi94) + (ys93_1*xo1u) * (1 + pi79) + (ys93_1*xo1d) * (1 + pi107),
pi94 == (ys94_1*xo1l) * (1 + pi93) + (ys94_1*xo1r) * (1 + pi95) + (ys94_1*xo1u) * (1 + pi80) + (ys94_1*xo1d) * (1 + pi108),
pi95 == (ys95_1*xo1l) * (1 + pi94) + (ys95_1*xo1r) * (1 + pi96) + (ys95_1*xo1u) * (1 + pi81) + (ys95_1*xo1d) * (1 + pi109),
pi96 == (ys96_1*xo1l) * (1 + pi95) + (ys96_1*xo1r) * (1 + pi97) + (ys96_1*xo1u) * (1 + pi82) + (ys96_1*xo1d) * (1 + pi110),
pi97 == (ys97_1*xo1l) * (1 + pi96) + (ys97_1*xo1r) * (1 + pi97) + (ys97_1*xo1u) * (1 + pi83) + (ys97_1*xo1d) * (1 + pi111),
pi98 == (ys98_1*xo1l) * (1 + pi98) + (ys98_1*xo1r) * (1 + pi99) + (ys98_1*xo1u) * (1 + pi84) + (ys98_1*xo1d) * (1 + pi112),
pi99 == (ys99_1*xo1l) * (1 + pi98) + (ys99_1*xo1r) * (1 + pi100) + (ys99_1*xo1u) * (1 + pi85) + (ys99_1*xo1d) * (1 + pi113),
pi100 == (ys100_1*xo1l) * (1 + pi99) + (ys100_1*xo1r) * (1 + pi101) + (ys100_1*xo1u) * (1 + pi86) + (ys100_1*xo1d) * (1 + pi114),
pi101 == (ys101_1*xo1l) * (1 + pi100) + (ys101_1*xo1r) * (1 + pi102) + (ys101_1*xo1u) * (1 + pi87) + (ys101_1*xo1d) * (1 + pi115),
pi102 == (ys102_1*xo1l) * (1 + pi101) + (ys102_1*xo1r) * (1 + pi103) + (ys102_1*xo1u) * (1 + pi88) + (ys102_1*xo1d) * (1 + pi116),
pi103 == (ys103_1*xo1l) * (1 + pi102) + (ys103_1*xo1r) * (1 + pi104) + (ys103_1*xo1u) * (1 + pi89) + (ys103_1*xo1d) * (1 + pi117),
pi104 == (ys104_1*xo1l) * (1 + pi103) + (ys104_1*xo1r) * (1 + pi105) + (ys104_1*xo1u) * (1 + pi90) + (ys104_1*xo1d) * (1 + pi118),
pi105 == (ys105_1*xo1l) * (1 + pi104) + (ys105_1*xo1r) * (1 + pi106) + (ys105_1*xo1u) * (1 + pi91) + (ys105_1*xo1d) * (1 + pi119),
pi106 == (ys106_1*xo1l) * (1 + pi105) + (ys106_1*xo1r) * (1 + pi107) + (ys106_1*xo1u) * (1 + pi92) + (ys106_1*xo1d) * (1 + pi120),
pi107 == (ys107_1*xo1l) * (1 + pi106) + (ys107_1*xo1r) * (1 + pi108) + (ys107_1*xo1u) * (1 + pi93) + (ys107_1*xo1d) * (1 + pi121),
pi108 == (ys108_1*xo1l) * (1 + pi107) + (ys108_1*xo1r) * (1 + pi109) + (ys108_1*xo1u) * (1 + pi94) + (ys108_1*xo1d) * (1 + pi122),
pi109 == (ys109_1*xo1l) * (1 + pi108) + (ys109_1*xo1r) * (1 + pi110) + (ys109_1*xo1u) * (1 + pi95) + (ys109_1*xo1d) * (1 + pi123),
pi110 == (ys110_1*xo1l) * (1 + pi109) + (ys110_1*xo1r) * (1 + pi111) + (ys110_1*xo1u) * (1 + pi96) + (ys110_1*xo1d) * (1 + pi124),
pi111 == (ys111_1*xo1l) * (1 + pi110) + (ys111_1*xo1r) * (1 + pi111) + (ys111_1*xo1u) * (1 + pi97) + (ys111_1*xo1d) * (1 + pi125),
pi112 == (ys112_1*xo1l) * (1 + pi112) + (ys112_1*xo1r) * (1 + pi113) + (ys112_1*xo1u) * (1 + pi98) + (ys112_1*xo1d) * (1 + pi126),
pi113 == (ys113_1*xo1l) * (1 + pi112) + (ys113_1*xo1r) * (1 + pi114) + (ys113_1*xo1u) * (1 + pi99) + (ys113_1*xo1d) * (1 + pi127),
pi114 == (ys114_1*xo1l) * (1 + pi113) + (ys114_1*xo1r) * (1 + pi115) + (ys114_1*xo1u) * (1 + pi100) + (ys114_1*xo1d) * (1 + pi128),
pi115 == (ys115_1*xo1l) * (1 + pi114) + (ys115_1*xo1r) * (1 + pi116) + (ys115_1*xo1u) * (1 + pi101) + (ys115_1*xo1d) * (1 + pi129),
pi116 == (ys116_1*xo1l) * (1 + pi115) + (ys116_1*xo1r) * (1 + pi117) + (ys116_1*xo1u) * (1 + pi102) + (ys116_1*xo1d) * (1 + pi130),
pi117 == (ys117_1*xo1l) * (1 + pi116) + (ys117_1*xo1r) * (1 + pi118) + (ys117_1*xo1u) * (1 + pi103) + (ys117_1*xo1d) * (1 + pi131),
pi118 == (ys118_1*xo1l) * (1 + pi117) + (ys118_1*xo1r) * (1 + pi119) + (ys118_1*xo1u) * (1 + pi104) + (ys118_1*xo1d) * (1 + pi132),
pi119 == (ys119_1*xo1l) * (1 + pi118) + (ys119_1*xo1r) * (1 + pi120) + (ys119_1*xo1u) * (1 + pi105) + (ys119_1*xo1d) * (1 + pi133),
pi120 == (ys120_1*xo1l) * (1 + pi119) + (ys120_1*xo1r) * (1 + pi121) + (ys120_1*xo1u) * (1 + pi106) + (ys120_1*xo1d) * (1 + pi134),
pi121 == (ys121_1*xo1l) * (1 + pi120) + (ys121_1*xo1r) * (1 + pi122) + (ys121_1*xo1u) * (1 + pi107) + (ys121_1*xo1d) * (1 + pi135),
pi122 == (ys122_1*xo1l) * (1 + pi121) + (ys122_1*xo1r) * (1 + pi123) + (ys122_1*xo1u) * (1 + pi108) + (ys122_1*xo1d) * (1 + pi136),
pi123 == (ys123_1*xo1l) * (1 + pi122) + (ys123_1*xo1r) * (1 + pi124) + (ys123_1*xo1u) * (1 + pi109) + (ys123_1*xo1d) * (1 + pi137),
pi124 == (ys124_1*xo1l) * (1 + pi123) + (ys124_1*xo1r) * (1 + pi125) + (ys124_1*xo1u) * (1 + pi110) + (ys124_1*xo1d) * (1 + pi138),
pi125 == (ys125_1*xo1l) * (1 + pi124) + (ys125_1*xo1r) * (1 + pi125) + (ys125_1*xo1u) * (1 + pi111) + (ys125_1*xo1d) * (1 + pi139),
pi126 == (ys126_1*xo1l) * (1 + pi126) + (ys126_1*xo1r) * (1 + pi127) + (ys126_1*xo1u) * (1 + pi112) + (ys126_1*xo1d) * (1 + pi140),
pi127 == (ys127_1*xo1l) * (1 + pi126) + (ys127_1*xo1r) * (1 + pi128) + (ys127_1*xo1u) * (1 + pi113) + (ys127_1*xo1d) * (1 + pi141),
pi128 == (ys128_1*xo1l) * (1 + pi127) + (ys128_1*xo1r) * (1 + pi129) + (ys128_1*xo1u) * (1 + pi114) + (ys128_1*xo1d) * (1 + pi142),
pi129 == (ys129_1*xo1l) * (1 + pi128) + (ys129_1*xo1r) * (1 + pi130) + (ys129_1*xo1u) * (1 + pi115) + (ys129_1*xo1d) * (1 + pi143),
pi130 == (ys130_1*xo1l) * (1 + pi129) + (ys130_1*xo1r) * (1 + pi131) + (ys130_1*xo1u) * (1 + pi116) + (ys130_1*xo1d) * (1 + pi144),
pi131 == (ys131_1*xo1l) * (1 + pi130) + (ys131_1*xo1r) * (1 + pi132) + (ys131_1*xo1u) * (1 + pi117) + (ys131_1*xo1d) * (1 + pi145),
pi132 == (ys132_1*xo1l) * (1 + pi131) + (ys132_1*xo1r) * (1 + pi133) + (ys132_1*xo1u) * (1 + pi118) + (ys132_1*xo1d) * (1 + pi146),
pi133 == (ys133_1*xo1l) * (1 + pi132) + (ys133_1*xo1r) * (1 + pi134) + (ys133_1*xo1u) * (1 + pi119) + (ys133_1*xo1d) * (1 + pi147),
pi134 == (ys134_1*xo1l) * (1 + pi133) + (ys134_1*xo1r) * (1 + pi135) + (ys134_1*xo1u) * (1 + pi120) + (ys134_1*xo1d) * (1 + pi148),
pi135 == (ys135_1*xo1l) * (1 + pi134) + (ys135_1*xo1r) * (1 + pi136) + (ys135_1*xo1u) * (1 + pi121) + (ys135_1*xo1d) * (1 + pi149),
pi136 == (ys136_1*xo1l) * (1 + pi135) + (ys136_1*xo1r) * (1 + pi137) + (ys136_1*xo1u) * (1 + pi122) + (ys136_1*xo1d) * (1 + pi150),
pi137 == (ys137_1*xo1l) * (1 + pi136) + (ys137_1*xo1r) * (1 + pi138) + (ys137_1*xo1u) * (1 + pi123) + (ys137_1*xo1d) * (1 + pi151),
pi138 == (ys138_1*xo1l) * (1 + pi137) + (ys138_1*xo1r) * (1 + pi139) + (ys138_1*xo1u) * (1 + pi124) + (ys138_1*xo1d) * (1 + pi152),
pi139 == (ys139_1*xo1l) * (1 + pi138) + (ys139_1*xo1r) * (1 + pi139) + (ys139_1*xo1u) * (1 + pi125) + (ys139_1*xo1d) * (1 + pi153),
pi140 == (ys140_1*xo1l) * (1 + pi140) + (ys140_1*xo1r) * (1 + pi141) + (ys140_1*xo1u) * (1 + pi126) + (ys140_1*xo1d) * (1 + pi154),
pi141 == (ys141_1*xo1l) * (1 + pi140) + (ys141_1*xo1r) * (1 + pi142) + (ys141_1*xo1u) * (1 + pi127) + (ys141_1*xo1d) * (1 + pi155),
pi142 == (ys142_1*xo1l) * (1 + pi141) + (ys142_1*xo1r) * (1 + pi143) + (ys142_1*xo1u) * (1 + pi128) + (ys142_1*xo1d) * (1 + pi156),
pi143 == (ys143_1*xo1l) * (1 + pi142) + (ys143_1*xo1r) * (1 + pi144) + (ys143_1*xo1u) * (1 + pi129) + (ys143_1*xo1d) * (1 + pi157),
pi144 == (ys144_1*xo1l) * (1 + pi143) + (ys144_1*xo1r) * (1 + pi145) + (ys144_1*xo1u) * (1 + pi130) + (ys144_1*xo1d) * (1 + pi158),
pi145 == (ys145_1*xo1l) * (1 + pi144) + (ys145_1*xo1r) * (1 + pi146) + (ys145_1*xo1u) * (1 + pi131) + (ys145_1*xo1d) * (1 + pi159),
pi146 == (ys146_1*xo1l) * (1 + pi145) + (ys146_1*xo1r) * (1 + pi147) + (ys146_1*xo1u) * (1 + pi132) + (ys146_1*xo1d) * (1 + pi160),
pi147 == (ys147_1*xo1l) * (1 + pi146) + (ys147_1*xo1r) * (1 + pi148) + (ys147_1*xo1u) * (1 + pi133) + (ys147_1*xo1d) * (1 + pi161),
pi148 == (ys148_1*xo1l) * (1 + pi147) + (ys148_1*xo1r) * (1 + pi149) + (ys148_1*xo1u) * (1 + pi134) + (ys148_1*xo1d) * (1 + pi162),
pi149 == (ys149_1*xo1l) * (1 + pi148) + (ys149_1*xo1r) * (1 + pi150) + (ys149_1*xo1u) * (1 + pi135) + (ys149_1*xo1d) * (1 + pi163),
pi150 == (ys150_1*xo1l) * (1 + pi149) + (ys150_1*xo1r) * (1 + pi151) + (ys150_1*xo1u) * (1 + pi136) + (ys150_1*xo1d) * (1 + pi164),
pi151 == (ys151_1*xo1l) * (1 + pi150) + (ys151_1*xo1r) * (1 + pi152) + (ys151_1*xo1u) * (1 + pi137) + (ys151_1*xo1d) * (1 + pi165),
pi152 == (ys152_1*xo1l) * (1 + pi151) + (ys152_1*xo1r) * (1 + pi153) + (ys152_1*xo1u) * (1 + pi138) + (ys152_1*xo1d) * (1 + pi166),
pi153 == (ys153_1*xo1l) * (1 + pi152) + (ys153_1*xo1r) * (1 + pi153) + (ys153_1*xo1u) * (1 + pi139) + (ys153_1*xo1d) * (1 + pi167),
pi154 == (ys154_1*xo1l) * (1 + pi154) + (ys154_1*xo1r) * (1 + pi155) + (ys154_1*xo1u) * (1 + pi140) + (ys154_1*xo1d) * (1 + pi168),
pi155 == (ys155_1*xo1l) * (1 + pi154) + (ys155_1*xo1r) * (1 + pi156) + (ys155_1*xo1u) * (1 + pi141) + (ys155_1*xo1d) * (1 + pi169),
pi156 == (ys156_1*xo1l) * (1 + pi155) + (ys156_1*xo1r) * (1 + pi157) + (ys156_1*xo1u) * (1 + pi142) + (ys156_1*xo1d) * (1 + pi170),
pi157 == (ys157_1*xo1l) * (1 + pi156) + (ys157_1*xo1r) * (1 + pi158) + (ys157_1*xo1u) * (1 + pi143) + (ys157_1*xo1d) * (1 + pi171),
pi158 == (ys158_1*xo1l) * (1 + pi157) + (ys158_1*xo1r) * (1 + pi159) + (ys158_1*xo1u) * (1 + pi144) + (ys158_1*xo1d) * (1 + pi172),
pi159 == (ys159_1*xo1l) * (1 + pi158) + (ys159_1*xo1r) * (1 + pi160) + (ys159_1*xo1u) * (1 + pi145) + (ys159_1*xo1d) * (1 + pi173),
pi160 == (ys160_1*xo1l) * (1 + pi159) + (ys160_1*xo1r) * (1 + pi161) + (ys160_1*xo1u) * (1 + pi146) + (ys160_1*xo1d) * (1 + pi174),
pi161 == (ys161_1*xo1l) * (1 + pi160) + (ys161_1*xo1r) * (1 + pi162) + (ys161_1*xo1u) * (1 + pi147) + (ys161_1*xo1d) * (1 + pi175),
pi162 == (ys162_1*xo1l) * (1 + pi161) + (ys162_1*xo1r) * (1 + pi163) + (ys162_1*xo1u) * (1 + pi148) + (ys162_1*xo1d) * (1 + pi176),
pi163 == (ys163_1*xo1l) * (1 + pi162) + (ys163_1*xo1r) * (1 + pi164) + (ys163_1*xo1u) * (1 + pi149) + (ys163_1*xo1d) * (1 + pi177),
pi164 == (ys164_1*xo1l) * (1 + pi163) + (ys164_1*xo1r) * (1 + pi165) + (ys164_1*xo1u) * (1 + pi150) + (ys164_1*xo1d) * (1 + pi178),
pi165 == (ys165_1*xo1l) * (1 + pi164) + (ys165_1*xo1r) * (1 + pi166) + (ys165_1*xo1u) * (1 + pi151) + (ys165_1*xo1d) * (1 + pi179),
pi166 == (ys166_1*xo1l) * (1 + pi165) + (ys166_1*xo1r) * (1 + pi167) + (ys166_1*xo1u) * (1 + pi152) + (ys166_1*xo1d) * (1 + pi180),
pi167 == (ys167_1*xo1l) * (1 + pi166) + (ys167_1*xo1r) * (1 + pi167) + (ys167_1*xo1u) * (1 + pi153) + (ys167_1*xo1d) * (1 + pi181),
pi168 == (ys168_1*xo1l) * (1 + pi168) + (ys168_1*xo1r) * (1 + pi169) + (ys168_1*xo1u) * (1 + pi154) + (ys168_1*xo1d) * (1 + pi182),
pi169 == (ys169_1*xo1l) * (1 + pi168) + (ys169_1*xo1r) * (1 + pi170) + (ys169_1*xo1u) * (1 + pi155) + (ys169_1*xo1d) * (1 + pi183),
pi170 == (ys170_1*xo1l) * (1 + pi169) + (ys170_1*xo1r) * (1 + pi171) + (ys170_1*xo1u) * (1 + pi156) + (ys170_1*xo1d) * (1 + pi184),
pi171 == (ys171_1*xo1l) * (1 + pi170) + (ys171_1*xo1r) * (1 + pi172) + (ys171_1*xo1u) * (1 + pi157) + (ys171_1*xo1d) * (1 + pi185),
pi172 == (ys172_1*xo1l) * (1 + pi171) + (ys172_1*xo1r) * (1 + pi173) + (ys172_1*xo1u) * (1 + pi158) + (ys172_1*xo1d) * (1 + pi186),
pi173 == (ys173_1*xo1l) * (1 + pi172) + (ys173_1*xo1r) * (1 + pi174) + (ys173_1*xo1u) * (1 + pi159) + (ys173_1*xo1d) * (1 + pi187),
pi174 == (ys174_1*xo1l) * (1 + pi173) + (ys174_1*xo1r) * (1 + pi175) + (ys174_1*xo1u) * (1 + pi160) + (ys174_1*xo1d) * (1 + pi188),
pi175 == (ys175_1*xo1l) * (1 + pi174) + (ys175_1*xo1r) * (1 + pi176) + (ys175_1*xo1u) * (1 + pi161) + (ys175_1*xo1d) * (1 + pi189),
pi176 == (ys176_1*xo1l) * (1 + pi175) + (ys176_1*xo1r) * (1 + pi177) + (ys176_1*xo1u) * (1 + pi162) + (ys176_1*xo1d) * (1 + pi190),
pi177 == (ys177_1*xo1l) * (1 + pi176) + (ys177_1*xo1r) * (1 + pi178) + (ys177_1*xo1u) * (1 + pi163) + (ys177_1*xo1d) * (1 + pi191),
pi178 == (ys178_1*xo1l) * (1 + pi177) + (ys178_1*xo1r) * (1 + pi179) + (ys178_1*xo1u) * (1 + pi164) + (ys178_1*xo1d) * (1 + pi192),
pi179 == (ys179_1*xo1l) * (1 + pi178) + (ys179_1*xo1r) * (1 + pi180) + (ys179_1*xo1u) * (1 + pi165) + (ys179_1*xo1d) * (1 + pi193),
pi180 == (ys180_1*xo1l) * (1 + pi179) + (ys180_1*xo1r) * (1 + pi181) + (ys180_1*xo1u) * (1 + pi166) + (ys180_1*xo1d) * (1 + pi194),
pi181 == (ys181_1*xo1l) * (1 + pi180) + (ys181_1*xo1r) * (1 + pi181) + (ys181_1*xo1u) * (1 + pi167) + (ys181_1*xo1d) * (1 + pi195),
pi182 == (ys182_1*xo1l) * (1 + pi182) + (ys182_1*xo1r) * (1 + pi183) + (ys182_1*xo1u) * (1 + pi168) + (ys182_1*xo1d) * (1 + pi182),
pi183 == 0, 
pi184 == (ys184_1*xo1l) * (1 + pi183) + (ys184_1*xo1r) * (1 + pi185) + (ys184_1*xo1u) * (1 + pi170) + (ys184_1*xo1d) * (1 + pi184),
pi185 == (ys185_1*xo1l) * (1 + pi184) + (ys185_1*xo1r) * (1 + pi186) + (ys185_1*xo1u) * (1 + pi171) + (ys185_1*xo1d) * (1 + pi185),
pi186 == (ys186_1*xo1l) * (1 + pi185) + (ys186_1*xo1r) * (1 + pi187) + (ys186_1*xo1u) * (1 + pi172) + (ys186_1*xo1d) * (1 + pi186),
pi187 == (ys187_1*xo1l) * (1 + pi186) + (ys187_1*xo1r) * (1 + pi188) + (ys187_1*xo1u) * (1 + pi173) + (ys187_1*xo1d) * (1 + pi187),
pi188 == (ys188_1*xo1l) * (1 + pi187) + (ys188_1*xo1r) * (1 + pi189) + (ys188_1*xo1u) * (1 + pi174) + (ys188_1*xo1d) * (1 + pi188),
pi189 == (ys189_1*xo1l) * (1 + pi188) + (ys189_1*xo1r) * (1 + pi190) + (ys189_1*xo1u) * (1 + pi175) + (ys189_1*xo1d) * (1 + pi189),
pi190 == (ys190_1*xo1l) * (1 + pi189) + (ys190_1*xo1r) * (1 + pi191) + (ys190_1*xo1u) * (1 + pi176) + (ys190_1*xo1d) * (1 + pi190),
pi191 == (ys191_1*xo1l) * (1 + pi190) + (ys191_1*xo1r) * (1 + pi192) + (ys191_1*xo1u) * (1 + pi177) + (ys191_1*xo1d) * (1 + pi191),
pi192 == (ys192_1*xo1l) * (1 + pi191) + (ys192_1*xo1r) * (1 + pi193) + (ys192_1*xo1u) * (1 + pi178) + (ys192_1*xo1d) * (1 + pi192),
pi193 == (ys193_1*xo1l) * (1 + pi192) + (ys193_1*xo1r) * (1 + pi194) + (ys193_1*xo1u) * (1 + pi179) + (ys193_1*xo1d) * (1 + pi193),
pi194 == (ys194_1*xo1l) * (1 + pi193) + (ys194_1*xo1r) * (1 + pi195) + (ys194_1*xo1u) * (1 + pi180) + (ys194_1*xo1d) * (1 + pi194),
pi195 == (ys195_1*xo1l) * (1 + pi194) + (ys195_1*xo1r) * (1 + pi195) + (ys195_1*xo1u) * (1 + pi181) + (ys195_1*xo1d) * (1 + pi195),
exp==((pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi30+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47+pi48+pi49+pi50+pi51+pi52+pi53+pi54+pi55+pi56+pi57+pi58+pi59+pi60+pi61+pi62+pi63+pi64+pi65+pi66+pi67+pi68+pi69+pi70+pi71+pi72+pi73+pi74+pi75+pi76+pi77+pi78+pi79+pi80+pi81+pi82+pi83+pi84+pi85+pi86+pi87+pi88+pi89+pi90+pi91+pi92+pi93+pi94+pi95+pi96+pi97+pi98+pi99+pi100+pi101+pi102+pi103+pi104+pi105+pi106+pi107+pi108+pi109+pi110+pi111+pi112+pi113+pi114+pi115+pi116+pi117+pi118+pi119+pi120+pi121+pi122+pi123+pi124+pi125+pi126+pi127+pi128+pi129+pi130+pi131+pi132+pi133+pi134+pi135+pi136+pi137+pi138+pi139+pi140+pi141+pi142+pi143+pi144+pi145+pi146+pi147+pi148+pi149+pi150+pi151+pi152+pi153+pi154+pi155+pi156+pi157+pi158+pi159+pi160+pi161+pi162+pi163+pi164+pi165+pi166+pi167+pi168+pi169+pi170+pi171+pi172+pi173+pi174+pi175+pi176+pi177+pi178+pi179+pi180+pi181+pi182+pi184+pi185+pi186+pi187+pi188+pi189+pi190+pi191+pi192+pi193+pi194+pi195)) * Q(1,195),
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
xo1r== Q(9, 19),
xo1d== Q(9, 19),
xo1l== Q(1, 19),
xo1u + xo1r + xo1d + xo1l == 1,
# Assigned observables
ys1_1 == 1,
ys16_1 == 1,
ys29_1 == 1,
ys0_1 == 1,
ys15_1 == 1,
ys28_1 == 1,
ys2_1 == 1,
ys30_1 == 1,
ys14_1 == 1,
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
ys95_1 == 1,
ys96_1 == 1,
ys97_1 == 1,
ys98_1 == 1,
ys99_1 == 1,
ys100_1 == 1,
ys101_1 == 1,
ys102_1 == 1,
ys103_1 == 1,
ys104_1 == 1,
ys105_1 == 1,
ys106_1 == 1,
ys107_1 == 1,
ys108_1 == 1,
ys109_1 == 1,
ys110_1 == 1,
ys111_1 == 1,
ys112_1 == 1,
ys113_1 == 1,
ys114_1 == 1,
ys115_1 == 1,
ys116_1 == 1,
ys117_1 == 1,
ys118_1 == 1,
ys119_1 == 1,
ys120_1 == 1,
ys121_1 == 1,
ys122_1 == 1,
ys123_1 == 1,
ys124_1 == 1,
ys125_1 == 1,
ys126_1 == 1,
ys127_1 == 1,
ys128_1 == 1,
ys129_1 == 1,
ys130_1 == 1,
ys131_1 == 1,
ys132_1 == 1,
ys133_1 == 1,
ys134_1 == 1,
ys135_1 == 1,
ys136_1 == 1,
ys137_1 == 1,
ys138_1 == 1,
ys139_1 == 1,
ys140_1 == 1,
ys141_1 == 1,
ys142_1 == 1,
ys143_1 == 1,
ys144_1 == 1,
ys145_1 == 1,
ys146_1 == 1,
ys147_1 == 1,
ys148_1 == 1,
ys149_1 == 1,
ys150_1 == 1,
ys151_1 == 1,
ys152_1 == 1,
ys153_1 == 1,
ys154_1 == 1,
ys155_1 == 1,
ys156_1 == 1,
ys157_1 == 1,
ys158_1 == 1,
ys159_1 == 1,
ys160_1 == 1,
ys161_1 == 1,
ys162_1 == 1,
ys163_1 == 1,
ys164_1 == 1,
ys165_1 == 1,
ys166_1 == 1,
ys167_1 == 1,
ys168_1 == 1,
ys169_1 == 1,
ys170_1 == 1,
ys171_1 == 1,
ys172_1 == 1,
ys173_1 == 1,
ys174_1 == 1,
ys175_1 == 1,
ys176_1 == 1,
ys177_1 == 1,
ys178_1 == 1,
ys179_1 == 1,
ys180_1 == 1,
ys181_1 == 1,
ys182_1 == 1,
ys184_1 == 1,
ys185_1 == 1,
ys186_1 == 1,
ys187_1 == 1,
ys188_1 == 1,
ys189_1 == 1,
ys190_1 == 1,
ys191_1 == 1,
ys192_1 == 1,
ys193_1 == 1,
ys194_1 == 1,
ys195_1 == 1
)


sol = lambda : solver.model() if solver.check() == sat else "No Solution" if solver.check() == unsat else None
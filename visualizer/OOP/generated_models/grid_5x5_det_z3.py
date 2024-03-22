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
ys01 = Real('ys01')
ys02 = Real('ys02')
ys03 = Real('ys03')
ys04 = Real('ys04')
ys05 = Real('ys05')
ys06 = Real('ys06')
ys07 = Real('ys07')
ys08 = Real('ys08')
ys09 = Real('ys09')
ys010 = Real('ys010')
ys11 = Real('ys11')
ys12 = Real('ys12')
ys13 = Real('ys13')
ys14 = Real('ys14')
ys15 = Real('ys15')
ys16 = Real('ys16')
ys17 = Real('ys17')
ys18 = Real('ys18')
ys19 = Real('ys19')
ys110 = Real('ys110')
ys21 = Real('ys21')
ys22 = Real('ys22')
ys23 = Real('ys23')
ys24 = Real('ys24')
ys25 = Real('ys25')
ys26 = Real('ys26')
ys27 = Real('ys27')
ys28 = Real('ys28')
ys29 = Real('ys29')
ys210 = Real('ys210')
ys31 = Real('ys31')
ys32 = Real('ys32')
ys33 = Real('ys33')
ys34 = Real('ys34')
ys35 = Real('ys35')
ys36 = Real('ys36')
ys37 = Real('ys37')
ys38 = Real('ys38')
ys39 = Real('ys39')
ys310 = Real('ys310')
ys41 = Real('ys41')
ys42 = Real('ys42')
ys43 = Real('ys43')
ys44 = Real('ys44')
ys45 = Real('ys45')
ys46 = Real('ys46')
ys47 = Real('ys47')
ys48 = Real('ys48')
ys49 = Real('ys49')
ys410 = Real('ys410')
ys51 = Real('ys51')
ys52 = Real('ys52')
ys53 = Real('ys53')
ys54 = Real('ys54')
ys55 = Real('ys55')
ys56 = Real('ys56')
ys57 = Real('ys57')
ys58 = Real('ys58')
ys59 = Real('ys59')
ys510 = Real('ys510')
ys61 = Real('ys61')
ys62 = Real('ys62')
ys63 = Real('ys63')
ys64 = Real('ys64')
ys65 = Real('ys65')
ys66 = Real('ys66')
ys67 = Real('ys67')
ys68 = Real('ys68')
ys69 = Real('ys69')
ys610 = Real('ys610')
ys71 = Real('ys71')
ys72 = Real('ys72')
ys73 = Real('ys73')
ys74 = Real('ys74')
ys75 = Real('ys75')
ys76 = Real('ys76')
ys77 = Real('ys77')
ys78 = Real('ys78')
ys79 = Real('ys79')
ys710 = Real('ys710')
ys91 = Real('ys91')
ys92 = Real('ys92')
ys93 = Real('ys93')
ys94 = Real('ys94')
ys95 = Real('ys95')
ys96 = Real('ys96')
ys97 = Real('ys97')
ys98 = Real('ys98')
ys99 = Real('ys99')
ys910 = Real('ys910')
ys101 = Real('ys101')
ys102 = Real('ys102')
ys103 = Real('ys103')
ys104 = Real('ys104')
ys105 = Real('ys105')
ys106 = Real('ys106')
ys107 = Real('ys107')
ys108 = Real('ys108')
ys109 = Real('ys109')
ys1010 = Real('ys1010')
ys111 = Real('ys111')
ys112 = Real('ys112')
ys113 = Real('ys113')
ys114 = Real('ys114')
ys115 = Real('ys115')
ys116 = Real('ys116')
ys117 = Real('ys117')
ys118 = Real('ys118')
ys119 = Real('ys119')
ys1110 = Real('ys1110')
ys121 = Real('ys121')
ys122 = Real('ys122')
ys123 = Real('ys123')
ys124 = Real('ys124')
ys125 = Real('ys125')
ys126 = Real('ys126')
ys127 = Real('ys127')
ys128 = Real('ys128')
ys129 = Real('ys129')
ys1210 = Real('ys1210')
ys131 = Real('ys131')
ys132 = Real('ys132')
ys133 = Real('ys133')
ys134 = Real('ys134')
ys135 = Real('ys135')
ys136 = Real('ys136')
ys137 = Real('ys137')
ys138 = Real('ys138')
ys139 = Real('ys139')
ys1310 = Real('ys1310')
ys141 = Real('ys141')
ys142 = Real('ys142')
ys143 = Real('ys143')
ys144 = Real('ys144')
ys145 = Real('ys145')
ys146 = Real('ys146')
ys147 = Real('ys147')
ys148 = Real('ys148')
ys149 = Real('ys149')
ys1410 = Real('ys1410')
ys151 = Real('ys151')
ys152 = Real('ys152')
ys153 = Real('ys153')
ys154 = Real('ys154')
ys155 = Real('ys155')
ys156 = Real('ys156')
ys157 = Real('ys157')
ys158 = Real('ys158')
ys159 = Real('ys159')
ys1510 = Real('ys1510')
ys161 = Real('ys161')
ys162 = Real('ys162')
ys163 = Real('ys163')
ys164 = Real('ys164')
ys165 = Real('ys165')
ys166 = Real('ys166')
ys167 = Real('ys167')
ys168 = Real('ys168')
ys169 = Real('ys169')
ys1610 = Real('ys1610')
ys171 = Real('ys171')
ys172 = Real('ys172')
ys173 = Real('ys173')
ys174 = Real('ys174')
ys175 = Real('ys175')
ys176 = Real('ys176')
ys177 = Real('ys177')
ys178 = Real('ys178')
ys179 = Real('ys179')
ys1710 = Real('ys1710')
ys181 = Real('ys181')
ys182 = Real('ys182')
ys183 = Real('ys183')
ys184 = Real('ys184')
ys185 = Real('ys185')
ys186 = Real('ys186')
ys187 = Real('ys187')
ys188 = Real('ys188')
ys189 = Real('ys189')
ys1810 = Real('ys1810')
ys191 = Real('ys191')
ys192 = Real('ys192')
ys193 = Real('ys193')
ys194 = Real('ys194')
ys195 = Real('ys195')
ys196 = Real('ys196')
ys197 = Real('ys197')
ys198 = Real('ys198')
ys199 = Real('ys199')
ys1910 = Real('ys1910')
ys201 = Real('ys201')
ys202 = Real('ys202')
ys203 = Real('ys203')
ys204 = Real('ys204')
ys205 = Real('ys205')
ys206 = Real('ys206')
ys207 = Real('ys207')
ys208 = Real('ys208')
ys209 = Real('ys209')
ys2010 = Real('ys2010')
ys211 = Real('ys211')
ys212 = Real('ys212')
ys213 = Real('ys213')
ys214 = Real('ys214')
ys215 = Real('ys215')
ys216 = Real('ys216')
ys217 = Real('ys217')
ys218 = Real('ys218')
ys219 = Real('ys219')
ys2110 = Real('ys2110')
ys221 = Real('ys221')
ys222 = Real('ys222')
ys223 = Real('ys223')
ys224 = Real('ys224')
ys225 = Real('ys225')
ys226 = Real('ys226')
ys227 = Real('ys227')
ys228 = Real('ys228')
ys229 = Real('ys229')
ys2210 = Real('ys2210')
ys231 = Real('ys231')
ys232 = Real('ys232')
ys233 = Real('ys233')
ys234 = Real('ys234')
ys235 = Real('ys235')
ys236 = Real('ys236')
ys237 = Real('ys237')
ys238 = Real('ys238')
ys239 = Real('ys239')
ys2310 = Real('ys2310')
ys241 = Real('ys241')
ys242 = Real('ys242')
ys243 = Real('ys243')
ys244 = Real('ys244')
ys245 = Real('ys245')
ys246 = Real('ys246')
ys247 = Real('ys247')
ys248 = Real('ys248')
ys249 = Real('ys249')
ys2410 = Real('ys2410')

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
xo9l = Real('xo9l')
xo9r = Real('xo9r')
xo9u = Real('xo9u')
xo9d = Real('xo9d')
xo10l = Real('xo10l')
xo10r = Real('xo10r')
xo10u = Real('xo10u')
xo10d = Real('xo10d')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=4, pi1>=3, pi2>=2, pi3>=1, pi4>=1, pi5>=3, pi6>=2, pi7>=1, pi8>=0, pi9>=1, pi10>=3, pi11>=0, pi12>=1, pi13>=1, pi14>=2, pi15>=4, pi16>=3, pi17>=2, pi18>=2, pi19>=2, pi20>=5, pi21>=4, pi22>=3, pi23>=3, pi24>=4, 
# Expected cost/reard equations
pi0 == (ys01*xo1l + ys02*xo2l + ys03*xo3l + ys04*xo4l + ys05*xo5l + ys06*xo6l + ys07*xo7l + ys08*xo8l + ys09*xo9l + ys010*xo10l) * (1 + pi0) + (ys01*xo1r + ys02*xo2r + ys03*xo3r + ys04*xo4r + ys05*xo5r + ys06*xo6r + ys07*xo7r + ys08*xo8r + ys09*xo9r + ys010*xo10r) * (1 + pi1) + (ys01*xo1u + ys02*xo2u + ys03*xo3u + ys04*xo4u + ys05*xo5u + ys06*xo6u + ys07*xo7u + ys08*xo8u + ys09*xo9u + ys010*xo10u) * (1 + pi0) + (ys01*xo1d + ys02*xo2d + ys03*xo3d + ys04*xo4d + ys05*xo5d + ys06*xo6d + ys07*xo7d + ys08*xo8d + ys09*xo9d + ys010*xo10d) * (1 + pi5),
pi1 == (ys11*xo1l + ys12*xo2l + ys13*xo3l + ys14*xo4l + ys15*xo5l + ys16*xo6l + ys17*xo7l + ys18*xo8l + ys19*xo9l + ys110*xo10l) * (1 + pi0) + (ys11*xo1r + ys12*xo2r + ys13*xo3r + ys14*xo4r + ys15*xo5r + ys16*xo6r + ys17*xo7r + ys18*xo8r + ys19*xo9r + ys110*xo10r) * (1 + pi2) + (ys11*xo1u + ys12*xo2u + ys13*xo3u + ys14*xo4u + ys15*xo5u + ys16*xo6u + ys17*xo7u + ys18*xo8u + ys19*xo9u + ys110*xo10u) * (1 + pi1) + (ys11*xo1d + ys12*xo2d + ys13*xo3d + ys14*xo4d + ys15*xo5d + ys16*xo6d + ys17*xo7d + ys18*xo8d + ys19*xo9d + ys110*xo10d) * (1 + pi6),
pi2 == (ys21*xo1l + ys22*xo2l + ys23*xo3l + ys24*xo4l + ys25*xo5l + ys26*xo6l + ys27*xo7l + ys28*xo8l + ys29*xo9l + ys210*xo10l) * (1 + pi1) + (ys21*xo1r + ys22*xo2r + ys23*xo3r + ys24*xo4r + ys25*xo5r + ys26*xo6r + ys27*xo7r + ys28*xo8r + ys29*xo9r + ys210*xo10r) * (1 + pi3) + (ys21*xo1u + ys22*xo2u + ys23*xo3u + ys24*xo4u + ys25*xo5u + ys26*xo6u + ys27*xo7u + ys28*xo8u + ys29*xo9u + ys210*xo10u) * (1 + pi2) + (ys21*xo1d + ys22*xo2d + ys23*xo3d + ys24*xo4d + ys25*xo5d + ys26*xo6d + ys27*xo7d + ys28*xo8d + ys29*xo9d + ys210*xo10d) * (1 + pi7),
pi3 == (ys31*xo1l + ys32*xo2l + ys33*xo3l + ys34*xo4l + ys35*xo5l + ys36*xo6l + ys37*xo7l + ys38*xo8l + ys39*xo9l + ys310*xo10l) * (1 + pi2) + (ys31*xo1r + ys32*xo2r + ys33*xo3r + ys34*xo4r + ys35*xo5r + ys36*xo6r + ys37*xo7r + ys38*xo8r + ys39*xo9r + ys310*xo10r) * (1 + pi4) + (ys31*xo1u + ys32*xo2u + ys33*xo3u + ys34*xo4u + ys35*xo5u + ys36*xo6u + ys37*xo7u + ys38*xo8u + ys39*xo9u + ys310*xo10u) * (1 + pi3) + (ys31*xo1d + ys32*xo2d + ys33*xo3d + ys34*xo4d + ys35*xo5d + ys36*xo6d + ys37*xo7d + ys38*xo8d + ys39*xo9d + ys310*xo10d) * (1 + pi8),
pi4 == (ys41*xo1l + ys42*xo2l + ys43*xo3l + ys44*xo4l + ys45*xo5l + ys46*xo6l + ys47*xo7l + ys48*xo8l + ys49*xo9l + ys410*xo10l) * (1 + pi3) + (ys41*xo1r + ys42*xo2r + ys43*xo3r + ys44*xo4r + ys45*xo5r + ys46*xo6r + ys47*xo7r + ys48*xo8r + ys49*xo9r + ys410*xo10r) * (1 + pi4) + (ys41*xo1u + ys42*xo2u + ys43*xo3u + ys44*xo4u + ys45*xo5u + ys46*xo6u + ys47*xo7u + ys48*xo8u + ys49*xo9u + ys410*xo10u) * (1 + pi4) + (ys41*xo1d + ys42*xo2d + ys43*xo3d + ys44*xo4d + ys45*xo5d + ys46*xo6d + ys47*xo7d + ys48*xo8d + ys49*xo9d + ys410*xo10d) * (1 + pi9),
pi5 == (ys51*xo1l + ys52*xo2l + ys53*xo3l + ys54*xo4l + ys55*xo5l + ys56*xo6l + ys57*xo7l + ys58*xo8l + ys59*xo9l + ys510*xo10l) * (1 + pi5) + (ys51*xo1r + ys52*xo2r + ys53*xo3r + ys54*xo4r + ys55*xo5r + ys56*xo6r + ys57*xo7r + ys58*xo8r + ys59*xo9r + ys510*xo10r) * (1 + pi6) + (ys51*xo1u + ys52*xo2u + ys53*xo3u + ys54*xo4u + ys55*xo5u + ys56*xo6u + ys57*xo7u + ys58*xo8u + ys59*xo9u + ys510*xo10u) * (1 + pi0) + (ys51*xo1d + ys52*xo2d + ys53*xo3d + ys54*xo4d + ys55*xo5d + ys56*xo6d + ys57*xo7d + ys58*xo8d + ys59*xo9d + ys510*xo10d) * (1 + pi10),
pi6 == (ys61*xo1l + ys62*xo2l + ys63*xo3l + ys64*xo4l + ys65*xo5l + ys66*xo6l + ys67*xo7l + ys68*xo8l + ys69*xo9l + ys610*xo10l) * (1 + pi5) + (ys61*xo1r + ys62*xo2r + ys63*xo3r + ys64*xo4r + ys65*xo5r + ys66*xo6r + ys67*xo7r + ys68*xo8r + ys69*xo9r + ys610*xo10r) * (1 + pi7) + (ys61*xo1u + ys62*xo2u + ys63*xo3u + ys64*xo4u + ys65*xo5u + ys66*xo6u + ys67*xo7u + ys68*xo8u + ys69*xo9u + ys610*xo10u) * (1 + pi1) + (ys61*xo1d + ys62*xo2d + ys63*xo3d + ys64*xo4d + ys65*xo5d + ys66*xo6d + ys67*xo7d + ys68*xo8d + ys69*xo9d + ys610*xo10d) * (1 + pi11),
pi7 == (ys71*xo1l + ys72*xo2l + ys73*xo3l + ys74*xo4l + ys75*xo5l + ys76*xo6l + ys77*xo7l + ys78*xo8l + ys79*xo9l + ys710*xo10l) * (1 + pi6) + (ys71*xo1r + ys72*xo2r + ys73*xo3r + ys74*xo4r + ys75*xo5r + ys76*xo6r + ys77*xo7r + ys78*xo8r + ys79*xo9r + ys710*xo10r) * (1 + pi8) + (ys71*xo1u + ys72*xo2u + ys73*xo3u + ys74*xo4u + ys75*xo5u + ys76*xo6u + ys77*xo7u + ys78*xo8u + ys79*xo9u + ys710*xo10u) * (1 + pi2) + (ys71*xo1d + ys72*xo2d + ys73*xo3d + ys74*xo4d + ys75*xo5d + ys76*xo6d + ys77*xo7d + ys78*xo8d + ys79*xo9d + ys710*xo10d) * (1 + pi12),
pi8 == 0, 
pi9 == (ys91*xo1l + ys92*xo2l + ys93*xo3l + ys94*xo4l + ys95*xo5l + ys96*xo6l + ys97*xo7l + ys98*xo8l + ys99*xo9l + ys910*xo10l) * (1 + pi8) + (ys91*xo1r + ys92*xo2r + ys93*xo3r + ys94*xo4r + ys95*xo5r + ys96*xo6r + ys97*xo7r + ys98*xo8r + ys99*xo9r + ys910*xo10r) * (1 + pi9) + (ys91*xo1u + ys92*xo2u + ys93*xo3u + ys94*xo4u + ys95*xo5u + ys96*xo6u + ys97*xo7u + ys98*xo8u + ys99*xo9u + ys910*xo10u) * (1 + pi4) + (ys91*xo1d + ys92*xo2d + ys93*xo3d + ys94*xo4d + ys95*xo5d + ys96*xo6d + ys97*xo7d + ys98*xo8d + ys99*xo9d + ys910*xo10d) * (1 + pi14),
pi10 == (ys101*xo1l + ys102*xo2l + ys103*xo3l + ys104*xo4l + ys105*xo5l + ys106*xo6l + ys107*xo7l + ys108*xo8l + ys109*xo9l + ys1010*xo10l) * (1 + pi10) + (ys101*xo1r + ys102*xo2r + ys103*xo3r + ys104*xo4r + ys105*xo5r + ys106*xo6r + ys107*xo7r + ys108*xo8r + ys109*xo9r + ys1010*xo10r) * (1 + pi11) + (ys101*xo1u + ys102*xo2u + ys103*xo3u + ys104*xo4u + ys105*xo5u + ys106*xo6u + ys107*xo7u + ys108*xo8u + ys109*xo9u + ys1010*xo10u) * (1 + pi5) + (ys101*xo1d + ys102*xo2d + ys103*xo3d + ys104*xo4d + ys105*xo5d + ys106*xo6d + ys107*xo7d + ys108*xo8d + ys109*xo9d + ys1010*xo10d) * (1 + pi15),
pi11 == (ys111*xo1l + ys112*xo2l + ys113*xo3l + ys114*xo4l + ys115*xo5l + ys116*xo6l + ys117*xo7l + ys118*xo8l + ys119*xo9l + ys1110*xo10l) * (1 + pi10) + (ys111*xo1r + ys112*xo2r + ys113*xo3r + ys114*xo4r + ys115*xo5r + ys116*xo6r + ys117*xo7r + ys118*xo8r + ys119*xo9r + ys1110*xo10r) * (1 + pi12) + (ys111*xo1u + ys112*xo2u + ys113*xo3u + ys114*xo4u + ys115*xo5u + ys116*xo6u + ys117*xo7u + ys118*xo8u + ys119*xo9u + ys1110*xo10u) * (1 + pi6) + (ys111*xo1d + ys112*xo2d + ys113*xo3d + ys114*xo4d + ys115*xo5d + ys116*xo6d + ys117*xo7d + ys118*xo8d + ys119*xo9d + ys1110*xo10d) * (1 + pi16),
pi12 == (ys121*xo1l + ys122*xo2l + ys123*xo3l + ys124*xo4l + ys125*xo5l + ys126*xo6l + ys127*xo7l + ys128*xo8l + ys129*xo9l + ys1210*xo10l) * (1 + pi11) + (ys121*xo1r + ys122*xo2r + ys123*xo3r + ys124*xo4r + ys125*xo5r + ys126*xo6r + ys127*xo7r + ys128*xo8r + ys129*xo9r + ys1210*xo10r) * (1 + pi13) + (ys121*xo1u + ys122*xo2u + ys123*xo3u + ys124*xo4u + ys125*xo5u + ys126*xo6u + ys127*xo7u + ys128*xo8u + ys129*xo9u + ys1210*xo10u) * (1 + pi7) + (ys121*xo1d + ys122*xo2d + ys123*xo3d + ys124*xo4d + ys125*xo5d + ys126*xo6d + ys127*xo7d + ys128*xo8d + ys129*xo9d + ys1210*xo10d) * (1 + pi17),
pi13 == (ys131*xo1l + ys132*xo2l + ys133*xo3l + ys134*xo4l + ys135*xo5l + ys136*xo6l + ys137*xo7l + ys138*xo8l + ys139*xo9l + ys1310*xo10l) * (1 + pi12) + (ys131*xo1r + ys132*xo2r + ys133*xo3r + ys134*xo4r + ys135*xo5r + ys136*xo6r + ys137*xo7r + ys138*xo8r + ys139*xo9r + ys1310*xo10r) * (1 + pi14) + (ys131*xo1u + ys132*xo2u + ys133*xo3u + ys134*xo4u + ys135*xo5u + ys136*xo6u + ys137*xo7u + ys138*xo8u + ys139*xo9u + ys1310*xo10u) * (1 + pi8) + (ys131*xo1d + ys132*xo2d + ys133*xo3d + ys134*xo4d + ys135*xo5d + ys136*xo6d + ys137*xo7d + ys138*xo8d + ys139*xo9d + ys1310*xo10d) * (1 + pi18),
pi14 == (ys141*xo1l + ys142*xo2l + ys143*xo3l + ys144*xo4l + ys145*xo5l + ys146*xo6l + ys147*xo7l + ys148*xo8l + ys149*xo9l + ys1410*xo10l) * (1 + pi13) + (ys141*xo1r + ys142*xo2r + ys143*xo3r + ys144*xo4r + ys145*xo5r + ys146*xo6r + ys147*xo7r + ys148*xo8r + ys149*xo9r + ys1410*xo10r) * (1 + pi14) + (ys141*xo1u + ys142*xo2u + ys143*xo3u + ys144*xo4u + ys145*xo5u + ys146*xo6u + ys147*xo7u + ys148*xo8u + ys149*xo9u + ys1410*xo10u) * (1 + pi9) + (ys141*xo1d + ys142*xo2d + ys143*xo3d + ys144*xo4d + ys145*xo5d + ys146*xo6d + ys147*xo7d + ys148*xo8d + ys149*xo9d + ys1410*xo10d) * (1 + pi19),
pi15 == (ys151*xo1l + ys152*xo2l + ys153*xo3l + ys154*xo4l + ys155*xo5l + ys156*xo6l + ys157*xo7l + ys158*xo8l + ys159*xo9l + ys1510*xo10l) * (1 + pi15) + (ys151*xo1r + ys152*xo2r + ys153*xo3r + ys154*xo4r + ys155*xo5r + ys156*xo6r + ys157*xo7r + ys158*xo8r + ys159*xo9r + ys1510*xo10r) * (1 + pi16) + (ys151*xo1u + ys152*xo2u + ys153*xo3u + ys154*xo4u + ys155*xo5u + ys156*xo6u + ys157*xo7u + ys158*xo8u + ys159*xo9u + ys1510*xo10u) * (1 + pi10) + (ys151*xo1d + ys152*xo2d + ys153*xo3d + ys154*xo4d + ys155*xo5d + ys156*xo6d + ys157*xo7d + ys158*xo8d + ys159*xo9d + ys1510*xo10d) * (1 + pi20),
pi16 == (ys161*xo1l + ys162*xo2l + ys163*xo3l + ys164*xo4l + ys165*xo5l + ys166*xo6l + ys167*xo7l + ys168*xo8l + ys169*xo9l + ys1610*xo10l) * (1 + pi15) + (ys161*xo1r + ys162*xo2r + ys163*xo3r + ys164*xo4r + ys165*xo5r + ys166*xo6r + ys167*xo7r + ys168*xo8r + ys169*xo9r + ys1610*xo10r) * (1 + pi17) + (ys161*xo1u + ys162*xo2u + ys163*xo3u + ys164*xo4u + ys165*xo5u + ys166*xo6u + ys167*xo7u + ys168*xo8u + ys169*xo9u + ys1610*xo10u) * (1 + pi11) + (ys161*xo1d + ys162*xo2d + ys163*xo3d + ys164*xo4d + ys165*xo5d + ys166*xo6d + ys167*xo7d + ys168*xo8d + ys169*xo9d + ys1610*xo10d) * (1 + pi21),
pi17 == (ys171*xo1l + ys172*xo2l + ys173*xo3l + ys174*xo4l + ys175*xo5l + ys176*xo6l + ys177*xo7l + ys178*xo8l + ys179*xo9l + ys1710*xo10l) * (1 + pi16) + (ys171*xo1r + ys172*xo2r + ys173*xo3r + ys174*xo4r + ys175*xo5r + ys176*xo6r + ys177*xo7r + ys178*xo8r + ys179*xo9r + ys1710*xo10r) * (1 + pi18) + (ys171*xo1u + ys172*xo2u + ys173*xo3u + ys174*xo4u + ys175*xo5u + ys176*xo6u + ys177*xo7u + ys178*xo8u + ys179*xo9u + ys1710*xo10u) * (1 + pi12) + (ys171*xo1d + ys172*xo2d + ys173*xo3d + ys174*xo4d + ys175*xo5d + ys176*xo6d + ys177*xo7d + ys178*xo8d + ys179*xo9d + ys1710*xo10d) * (1 + pi22),
pi18 == (ys181*xo1l + ys182*xo2l + ys183*xo3l + ys184*xo4l + ys185*xo5l + ys186*xo6l + ys187*xo7l + ys188*xo8l + ys189*xo9l + ys1810*xo10l) * (1 + pi17) + (ys181*xo1r + ys182*xo2r + ys183*xo3r + ys184*xo4r + ys185*xo5r + ys186*xo6r + ys187*xo7r + ys188*xo8r + ys189*xo9r + ys1810*xo10r) * (1 + pi19) + (ys181*xo1u + ys182*xo2u + ys183*xo3u + ys184*xo4u + ys185*xo5u + ys186*xo6u + ys187*xo7u + ys188*xo8u + ys189*xo9u + ys1810*xo10u) * (1 + pi13) + (ys181*xo1d + ys182*xo2d + ys183*xo3d + ys184*xo4d + ys185*xo5d + ys186*xo6d + ys187*xo7d + ys188*xo8d + ys189*xo9d + ys1810*xo10d) * (1 + pi23),
pi19 == (ys191*xo1l + ys192*xo2l + ys193*xo3l + ys194*xo4l + ys195*xo5l + ys196*xo6l + ys197*xo7l + ys198*xo8l + ys199*xo9l + ys1910*xo10l) * (1 + pi18) + (ys191*xo1r + ys192*xo2r + ys193*xo3r + ys194*xo4r + ys195*xo5r + ys196*xo6r + ys197*xo7r + ys198*xo8r + ys199*xo9r + ys1910*xo10r) * (1 + pi19) + (ys191*xo1u + ys192*xo2u + ys193*xo3u + ys194*xo4u + ys195*xo5u + ys196*xo6u + ys197*xo7u + ys198*xo8u + ys199*xo9u + ys1910*xo10u) * (1 + pi14) + (ys191*xo1d + ys192*xo2d + ys193*xo3d + ys194*xo4d + ys195*xo5d + ys196*xo6d + ys197*xo7d + ys198*xo8d + ys199*xo9d + ys1910*xo10d) * (1 + pi24),
pi20 == (ys201*xo1l + ys202*xo2l + ys203*xo3l + ys204*xo4l + ys205*xo5l + ys206*xo6l + ys207*xo7l + ys208*xo8l + ys209*xo9l + ys2010*xo10l) * (1 + pi20) + (ys201*xo1r + ys202*xo2r + ys203*xo3r + ys204*xo4r + ys205*xo5r + ys206*xo6r + ys207*xo7r + ys208*xo8r + ys209*xo9r + ys2010*xo10r) * (1 + pi21) + (ys201*xo1u + ys202*xo2u + ys203*xo3u + ys204*xo4u + ys205*xo5u + ys206*xo6u + ys207*xo7u + ys208*xo8u + ys209*xo9u + ys2010*xo10u) * (1 + pi15) + (ys201*xo1d + ys202*xo2d + ys203*xo3d + ys204*xo4d + ys205*xo5d + ys206*xo6d + ys207*xo7d + ys208*xo8d + ys209*xo9d + ys2010*xo10d) * (1 + pi20),
pi21 == (ys211*xo1l + ys212*xo2l + ys213*xo3l + ys214*xo4l + ys215*xo5l + ys216*xo6l + ys217*xo7l + ys218*xo8l + ys219*xo9l + ys2110*xo10l) * (1 + pi20) + (ys211*xo1r + ys212*xo2r + ys213*xo3r + ys214*xo4r + ys215*xo5r + ys216*xo6r + ys217*xo7r + ys218*xo8r + ys219*xo9r + ys2110*xo10r) * (1 + pi22) + (ys211*xo1u + ys212*xo2u + ys213*xo3u + ys214*xo4u + ys215*xo5u + ys216*xo6u + ys217*xo7u + ys218*xo8u + ys219*xo9u + ys2110*xo10u) * (1 + pi16) + (ys211*xo1d + ys212*xo2d + ys213*xo3d + ys214*xo4d + ys215*xo5d + ys216*xo6d + ys217*xo7d + ys218*xo8d + ys219*xo9d + ys2110*xo10d) * (1 + pi21),
pi22 == (ys221*xo1l + ys222*xo2l + ys223*xo3l + ys224*xo4l + ys225*xo5l + ys226*xo6l + ys227*xo7l + ys228*xo8l + ys229*xo9l + ys2210*xo10l) * (1 + pi21) + (ys221*xo1r + ys222*xo2r + ys223*xo3r + ys224*xo4r + ys225*xo5r + ys226*xo6r + ys227*xo7r + ys228*xo8r + ys229*xo9r + ys2210*xo10r) * (1 + pi23) + (ys221*xo1u + ys222*xo2u + ys223*xo3u + ys224*xo4u + ys225*xo5u + ys226*xo6u + ys227*xo7u + ys228*xo8u + ys229*xo9u + ys2210*xo10u) * (1 + pi17) + (ys221*xo1d + ys222*xo2d + ys223*xo3d + ys224*xo4d + ys225*xo5d + ys226*xo6d + ys227*xo7d + ys228*xo8d + ys229*xo9d + ys2210*xo10d) * (1 + pi22),
pi23 == (ys231*xo1l + ys232*xo2l + ys233*xo3l + ys234*xo4l + ys235*xo5l + ys236*xo6l + ys237*xo7l + ys238*xo8l + ys239*xo9l + ys2310*xo10l) * (1 + pi22) + (ys231*xo1r + ys232*xo2r + ys233*xo3r + ys234*xo4r + ys235*xo5r + ys236*xo6r + ys237*xo7r + ys238*xo8r + ys239*xo9r + ys2310*xo10r) * (1 + pi24) + (ys231*xo1u + ys232*xo2u + ys233*xo3u + ys234*xo4u + ys235*xo5u + ys236*xo6u + ys237*xo7u + ys238*xo8u + ys239*xo9u + ys2310*xo10u) * (1 + pi18) + (ys231*xo1d + ys232*xo2d + ys233*xo3d + ys234*xo4d + ys235*xo5d + ys236*xo6d + ys237*xo7d + ys238*xo8d + ys239*xo9d + ys2310*xo10d) * (1 + pi23),
pi24 == (ys241*xo1l + ys242*xo2l + ys243*xo3l + ys244*xo4l + ys245*xo5l + ys246*xo6l + ys247*xo7l + ys248*xo8l + ys249*xo9l + ys2410*xo10l) * (1 + pi23) + (ys241*xo1r + ys242*xo2r + ys243*xo3r + ys244*xo4r + ys245*xo5r + ys246*xo6r + ys247*xo7r + ys248*xo8r + ys249*xo9r + ys2410*xo10r) * (1 + pi24) + (ys241*xo1u + ys242*xo2u + ys243*xo3u + ys244*xo4u + ys245*xo5u + ys246*xo6u + ys247*xo7u + ys248*xo8u + ys249*xo9u + ys2410*xo10u) * (1 + pi19) + (ys241*xo1d + ys242*xo2d + ys243*xo3d + ys244*xo4d + ys245*xo5d + ys246*xo6d + ys247*xo7d + ys248*xo8d + ys249*xo9d + ys2410*xo10d) * (1 + pi24),
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= 5
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24) * Q(1,24) <= 5,
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
xo9l>= 0,
xo9l<= 1,
xo9r>= 0,
xo9r<= 1,
xo9u>= 0,
xo9u<= 1,
xo9d>= 0,
xo9d<= 1,
xo10l>= 0,
xo10l<= 1,
xo10r>= 0,
xo10r<= 1,
xo10u>= 0,
xo10u<= 1,
xo10d>= 0,
xo10d<= 1,
xo1l + xo1r + xo1u + xo1d == 1,
xo2l + xo2r + xo2u + xo2d == 1,
xo3l + xo3r + xo3u + xo3d == 1,
xo4l + xo4r + xo4u + xo4d == 1,
xo5l + xo5r + xo5u + xo5d == 1,
xo6l + xo6r + xo6u + xo6d == 1,
xo7l + xo7r + xo7u + xo7d == 1,
xo8l + xo8r + xo8u + xo8d == 1,
xo9l + xo9r + xo9u + xo9d == 1,
xo10l + xo10r + xo10u + xo10d == 1,
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
Or(xo9l == 0, xo9l == 1),
Or(xo9r == 0, xo9r == 1),
Or(xo9u == 0, xo9u == 1),
Or(xo9d == 0, xo9d == 1),
Or(xo10l == 0, xo10l == 1),
Or(xo10r == 0, xo10r == 1),
Or(xo10u == 0, xo10u == 1),
Or(xo10d == 0, xo10d == 1),
# ysNM is a function that should map every state N to some observable class M
Or(ys01== 0 , ys01== 1),
Or(ys02== 0 , ys02== 1),
Or(ys03== 0 , ys03== 1),
Or(ys04== 0 , ys04== 1),
Or(ys05== 0 , ys05== 1),
Or(ys06== 0 , ys06== 1),
Or(ys07== 0 , ys07== 1),
Or(ys08== 0 , ys08== 1),
Or(ys09== 0 , ys09== 1),
Or(ys010== 0 , ys010== 1),
Or(ys11== 0 , ys11== 1),
Or(ys12== 0 , ys12== 1),
Or(ys13== 0 , ys13== 1),
Or(ys14== 0 , ys14== 1),
Or(ys15== 0 , ys15== 1),
Or(ys16== 0 , ys16== 1),
Or(ys17== 0 , ys17== 1),
Or(ys18== 0 , ys18== 1),
Or(ys19== 0 , ys19== 1),
Or(ys110== 0 , ys110== 1),
Or(ys21== 0 , ys21== 1),
Or(ys22== 0 , ys22== 1),
Or(ys23== 0 , ys23== 1),
Or(ys24== 0 , ys24== 1),
Or(ys25== 0 , ys25== 1),
Or(ys26== 0 , ys26== 1),
Or(ys27== 0 , ys27== 1),
Or(ys28== 0 , ys28== 1),
Or(ys29== 0 , ys29== 1),
Or(ys210== 0 , ys210== 1),
Or(ys31== 0 , ys31== 1),
Or(ys32== 0 , ys32== 1),
Or(ys33== 0 , ys33== 1),
Or(ys34== 0 , ys34== 1),
Or(ys35== 0 , ys35== 1),
Or(ys36== 0 , ys36== 1),
Or(ys37== 0 , ys37== 1),
Or(ys38== 0 , ys38== 1),
Or(ys39== 0 , ys39== 1),
Or(ys310== 0 , ys310== 1),
Or(ys41== 0 , ys41== 1),
Or(ys42== 0 , ys42== 1),
Or(ys43== 0 , ys43== 1),
Or(ys44== 0 , ys44== 1),
Or(ys45== 0 , ys45== 1),
Or(ys46== 0 , ys46== 1),
Or(ys47== 0 , ys47== 1),
Or(ys48== 0 , ys48== 1),
Or(ys49== 0 , ys49== 1),
Or(ys410== 0 , ys410== 1),
Or(ys51== 0 , ys51== 1),
Or(ys52== 0 , ys52== 1),
Or(ys53== 0 , ys53== 1),
Or(ys54== 0 , ys54== 1),
Or(ys55== 0 , ys55== 1),
Or(ys56== 0 , ys56== 1),
Or(ys57== 0 , ys57== 1),
Or(ys58== 0 , ys58== 1),
Or(ys59== 0 , ys59== 1),
Or(ys510== 0 , ys510== 1),
Or(ys61== 0 , ys61== 1),
Or(ys62== 0 , ys62== 1),
Or(ys63== 0 , ys63== 1),
Or(ys64== 0 , ys64== 1),
Or(ys65== 0 , ys65== 1),
Or(ys66== 0 , ys66== 1),
Or(ys67== 0 , ys67== 1),
Or(ys68== 0 , ys68== 1),
Or(ys69== 0 , ys69== 1),
Or(ys610== 0 , ys610== 1),
Or(ys71== 0 , ys71== 1),
Or(ys72== 0 , ys72== 1),
Or(ys73== 0 , ys73== 1),
Or(ys74== 0 , ys74== 1),
Or(ys75== 0 , ys75== 1),
Or(ys76== 0 , ys76== 1),
Or(ys77== 0 , ys77== 1),
Or(ys78== 0 , ys78== 1),
Or(ys79== 0 , ys79== 1),
Or(ys710== 0 , ys710== 1),
Or(ys91== 0 , ys91== 1),
Or(ys92== 0 , ys92== 1),
Or(ys93== 0 , ys93== 1),
Or(ys94== 0 , ys94== 1),
Or(ys95== 0 , ys95== 1),
Or(ys96== 0 , ys96== 1),
Or(ys97== 0 , ys97== 1),
Or(ys98== 0 , ys98== 1),
Or(ys99== 0 , ys99== 1),
Or(ys910== 0 , ys910== 1),
Or(ys101== 0 , ys101== 1),
Or(ys102== 0 , ys102== 1),
Or(ys103== 0 , ys103== 1),
Or(ys104== 0 , ys104== 1),
Or(ys105== 0 , ys105== 1),
Or(ys106== 0 , ys106== 1),
Or(ys107== 0 , ys107== 1),
Or(ys108== 0 , ys108== 1),
Or(ys109== 0 , ys109== 1),
Or(ys1010== 0 , ys1010== 1),
Or(ys111== 0 , ys111== 1),
Or(ys112== 0 , ys112== 1),
Or(ys113== 0 , ys113== 1),
Or(ys114== 0 , ys114== 1),
Or(ys115== 0 , ys115== 1),
Or(ys116== 0 , ys116== 1),
Or(ys117== 0 , ys117== 1),
Or(ys118== 0 , ys118== 1),
Or(ys119== 0 , ys119== 1),
Or(ys1110== 0 , ys1110== 1),
Or(ys121== 0 , ys121== 1),
Or(ys122== 0 , ys122== 1),
Or(ys123== 0 , ys123== 1),
Or(ys124== 0 , ys124== 1),
Or(ys125== 0 , ys125== 1),
Or(ys126== 0 , ys126== 1),
Or(ys127== 0 , ys127== 1),
Or(ys128== 0 , ys128== 1),
Or(ys129== 0 , ys129== 1),
Or(ys1210== 0 , ys1210== 1),
Or(ys131== 0 , ys131== 1),
Or(ys132== 0 , ys132== 1),
Or(ys133== 0 , ys133== 1),
Or(ys134== 0 , ys134== 1),
Or(ys135== 0 , ys135== 1),
Or(ys136== 0 , ys136== 1),
Or(ys137== 0 , ys137== 1),
Or(ys138== 0 , ys138== 1),
Or(ys139== 0 , ys139== 1),
Or(ys1310== 0 , ys1310== 1),
Or(ys141== 0 , ys141== 1),
Or(ys142== 0 , ys142== 1),
Or(ys143== 0 , ys143== 1),
Or(ys144== 0 , ys144== 1),
Or(ys145== 0 , ys145== 1),
Or(ys146== 0 , ys146== 1),
Or(ys147== 0 , ys147== 1),
Or(ys148== 0 , ys148== 1),
Or(ys149== 0 , ys149== 1),
Or(ys1410== 0 , ys1410== 1),
Or(ys151== 0 , ys151== 1),
Or(ys152== 0 , ys152== 1),
Or(ys153== 0 , ys153== 1),
Or(ys154== 0 , ys154== 1),
Or(ys155== 0 , ys155== 1),
Or(ys156== 0 , ys156== 1),
Or(ys157== 0 , ys157== 1),
Or(ys158== 0 , ys158== 1),
Or(ys159== 0 , ys159== 1),
Or(ys1510== 0 , ys1510== 1),
Or(ys161== 0 , ys161== 1),
Or(ys162== 0 , ys162== 1),
Or(ys163== 0 , ys163== 1),
Or(ys164== 0 , ys164== 1),
Or(ys165== 0 , ys165== 1),
Or(ys166== 0 , ys166== 1),
Or(ys167== 0 , ys167== 1),
Or(ys168== 0 , ys168== 1),
Or(ys169== 0 , ys169== 1),
Or(ys1610== 0 , ys1610== 1),
Or(ys171== 0 , ys171== 1),
Or(ys172== 0 , ys172== 1),
Or(ys173== 0 , ys173== 1),
Or(ys174== 0 , ys174== 1),
Or(ys175== 0 , ys175== 1),
Or(ys176== 0 , ys176== 1),
Or(ys177== 0 , ys177== 1),
Or(ys178== 0 , ys178== 1),
Or(ys179== 0 , ys179== 1),
Or(ys1710== 0 , ys1710== 1),
Or(ys181== 0 , ys181== 1),
Or(ys182== 0 , ys182== 1),
Or(ys183== 0 , ys183== 1),
Or(ys184== 0 , ys184== 1),
Or(ys185== 0 , ys185== 1),
Or(ys186== 0 , ys186== 1),
Or(ys187== 0 , ys187== 1),
Or(ys188== 0 , ys188== 1),
Or(ys189== 0 , ys189== 1),
Or(ys1810== 0 , ys1810== 1),
Or(ys191== 0 , ys191== 1),
Or(ys192== 0 , ys192== 1),
Or(ys193== 0 , ys193== 1),
Or(ys194== 0 , ys194== 1),
Or(ys195== 0 , ys195== 1),
Or(ys196== 0 , ys196== 1),
Or(ys197== 0 , ys197== 1),
Or(ys198== 0 , ys198== 1),
Or(ys199== 0 , ys199== 1),
Or(ys1910== 0 , ys1910== 1),
Or(ys201== 0 , ys201== 1),
Or(ys202== 0 , ys202== 1),
Or(ys203== 0 , ys203== 1),
Or(ys204== 0 , ys204== 1),
Or(ys205== 0 , ys205== 1),
Or(ys206== 0 , ys206== 1),
Or(ys207== 0 , ys207== 1),
Or(ys208== 0 , ys208== 1),
Or(ys209== 0 , ys209== 1),
Or(ys2010== 0 , ys2010== 1),
Or(ys211== 0 , ys211== 1),
Or(ys212== 0 , ys212== 1),
Or(ys213== 0 , ys213== 1),
Or(ys214== 0 , ys214== 1),
Or(ys215== 0 , ys215== 1),
Or(ys216== 0 , ys216== 1),
Or(ys217== 0 , ys217== 1),
Or(ys218== 0 , ys218== 1),
Or(ys219== 0 , ys219== 1),
Or(ys2110== 0 , ys2110== 1),
Or(ys221== 0 , ys221== 1),
Or(ys222== 0 , ys222== 1),
Or(ys223== 0 , ys223== 1),
Or(ys224== 0 , ys224== 1),
Or(ys225== 0 , ys225== 1),
Or(ys226== 0 , ys226== 1),
Or(ys227== 0 , ys227== 1),
Or(ys228== 0 , ys228== 1),
Or(ys229== 0 , ys229== 1),
Or(ys2210== 0 , ys2210== 1),
Or(ys231== 0 , ys231== 1),
Or(ys232== 0 , ys232== 1),
Or(ys233== 0 , ys233== 1),
Or(ys234== 0 , ys234== 1),
Or(ys235== 0 , ys235== 1),
Or(ys236== 0 , ys236== 1),
Or(ys237== 0 , ys237== 1),
Or(ys238== 0 , ys238== 1),
Or(ys239== 0 , ys239== 1),
Or(ys2310== 0 , ys2310== 1),
Or(ys241== 0 , ys241== 1),
Or(ys242== 0 , ys242== 1),
Or(ys243== 0 , ys243== 1),
Or(ys244== 0 , ys244== 1),
Or(ys245== 0 , ys245== 1),
Or(ys246== 0 , ys246== 1),
Or(ys247== 0 , ys247== 1),
Or(ys248== 0 , ys248== 1),
Or(ys249== 0 , ys249== 1),
Or(ys2410== 0 , ys2410== 1),
# Every state should be mapped to exactly one equivalence class
ys01 + ys02 + ys03 + ys04 + ys05 + ys06 + ys07 + ys08 + ys09 + ys010 == 1,
ys11 + ys12 + ys13 + ys14 + ys15 + ys16 + ys17 + ys18 + ys19 + ys110 == 1,
ys21 + ys22 + ys23 + ys24 + ys25 + ys26 + ys27 + ys28 + ys29 + ys210 == 1,
ys31 + ys32 + ys33 + ys34 + ys35 + ys36 + ys37 + ys38 + ys39 + ys310 == 1,
ys41 + ys42 + ys43 + ys44 + ys45 + ys46 + ys47 + ys48 + ys49 + ys410 == 1,
ys51 + ys52 + ys53 + ys54 + ys55 + ys56 + ys57 + ys58 + ys59 + ys510 == 1,
ys61 + ys62 + ys63 + ys64 + ys65 + ys66 + ys67 + ys68 + ys69 + ys610 == 1,
ys71 + ys72 + ys73 + ys74 + ys75 + ys76 + ys77 + ys78 + ys79 + ys710 == 1,
ys91 + ys92 + ys93 + ys94 + ys95 + ys96 + ys97 + ys98 + ys99 + ys910 == 1,
ys101 + ys102 + ys103 + ys104 + ys105 + ys106 + ys107 + ys108 + ys109 + ys1010 == 1,
ys111 + ys112 + ys113 + ys114 + ys115 + ys116 + ys117 + ys118 + ys119 + ys1110 == 1,
ys121 + ys122 + ys123 + ys124 + ys125 + ys126 + ys127 + ys128 + ys129 + ys1210 == 1,
ys131 + ys132 + ys133 + ys134 + ys135 + ys136 + ys137 + ys138 + ys139 + ys1310 == 1,
ys141 + ys142 + ys143 + ys144 + ys145 + ys146 + ys147 + ys148 + ys149 + ys1410 == 1,
ys151 + ys152 + ys153 + ys154 + ys155 + ys156 + ys157 + ys158 + ys159 + ys1510 == 1,
ys161 + ys162 + ys163 + ys164 + ys165 + ys166 + ys167 + ys168 + ys169 + ys1610 == 1,
ys171 + ys172 + ys173 + ys174 + ys175 + ys176 + ys177 + ys178 + ys179 + ys1710 == 1,
ys181 + ys182 + ys183 + ys184 + ys185 + ys186 + ys187 + ys188 + ys189 + ys1810 == 1,
ys191 + ys192 + ys193 + ys194 + ys195 + ys196 + ys197 + ys198 + ys199 + ys1910 == 1,
ys201 + ys202 + ys203 + ys204 + ys205 + ys206 + ys207 + ys208 + ys209 + ys2010 == 1,
ys211 + ys212 + ys213 + ys214 + ys215 + ys216 + ys217 + ys218 + ys219 + ys2110 == 1,
ys221 + ys222 + ys223 + ys224 + ys225 + ys226 + ys227 + ys228 + ys229 + ys2210 == 1,
ys231 + ys232 + ys233 + ys234 + ys235 + ys236 + ys237 + ys238 + ys239 + ys2310 == 1,
ys241 + ys242 + ys243 + ys244 + ys245 + ys246 + ys247 + ys248 + ys249 + ys2410 == 1
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
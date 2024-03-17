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
ys01 = Real('ys01')
ys02 = Real('ys02')
ys11 = Real('ys11')
ys12 = Real('ys12')
ys31 = Real('ys31')
ys32 = Real('ys32')
ys41 = Real('ys41')
ys42 = Real('ys42')
ys51 = Real('ys51')
ys52 = Real('ys52')
ys61 = Real('ys61')
ys62 = Real('ys62')
ys71 = Real('ys71')
ys72 = Real('ys72')
ys81 = Real('ys81')
ys82 = Real('ys82')
ys91 = Real('ys91')
ys92 = Real('ys92')
ys101 = Real('ys101')
ys102 = Real('ys102')
ys111 = Real('ys111')
ys112 = Real('ys112')
ys121 = Real('ys121')
ys122 = Real('ys122')
ys131 = Real('ys131')
ys132 = Real('ys132')
ys141 = Real('ys141')
ys142 = Real('ys142')
ys151 = Real('ys151')
ys152 = Real('ys152')
ys161 = Real('ys161')
ys162 = Real('ys162')
ys171 = Real('ys171')
ys172 = Real('ys172')
ys181 = Real('ys181')
ys182 = Real('ys182')
ys191 = Real('ys191')
ys192 = Real('ys192')
ys201 = Real('ys201')
ys202 = Real('ys202')
ys211 = Real('ys211')
ys212 = Real('ys212')
ys221 = Real('ys221')
ys222 = Real('ys222')
ys231 = Real('ys231')
ys232 = Real('ys232')
ys241 = Real('ys241')
ys242 = Real('ys242')
ys251 = Real('ys251')
ys252 = Real('ys252')
ys261 = Real('ys261')
ys262 = Real('ys262')
ys271 = Real('ys271')
ys272 = Real('ys272')
ys281 = Real('ys281')
ys282 = Real('ys282')
ys291 = Real('ys291')
ys292 = Real('ys292')
ys301 = Real('ys301')
ys302 = Real('ys302')
ys311 = Real('ys311')
ys312 = Real('ys312')
ys321 = Real('ys321')
ys322 = Real('ys322')
ys331 = Real('ys331')
ys332 = Real('ys332')
ys341 = Real('ys341')
ys342 = Real('ys342')
ys351 = Real('ys351')
ys352 = Real('ys352')
ys361 = Real('ys361')
ys362 = Real('ys362')
ys371 = Real('ys371')
ys372 = Real('ys372')
ys381 = Real('ys381')
ys382 = Real('ys382')
ys391 = Real('ys391')
ys392 = Real('ys392')
ys401 = Real('ys401')
ys402 = Real('ys402')
ys411 = Real('ys411')
ys412 = Real('ys412')
ys421 = Real('ys421')
ys422 = Real('ys422')
ys431 = Real('ys431')
ys432 = Real('ys432')
ys441 = Real('ys441')
ys442 = Real('ys442')
ys451 = Real('ys451')
ys452 = Real('ys452')
ys461 = Real('ys461')
ys462 = Real('ys462')
ys471 = Real('ys471')
ys472 = Real('ys472')
ys481 = Real('ys481')
ys482 = Real('ys482')
ys491 = Real('ys491')
ys492 = Real('ys492')
ys501 = Real('ys501')
ys502 = Real('ys502')
ys511 = Real('ys511')
ys512 = Real('ys512')
ys521 = Real('ys521')
ys522 = Real('ys522')
ys531 = Real('ys531')
ys532 = Real('ys532')
ys541 = Real('ys541')
ys542 = Real('ys542')
ys551 = Real('ys551')
ys552 = Real('ys552')
ys561 = Real('ys561')
ys562 = Real('ys562')
ys571 = Real('ys571')
ys572 = Real('ys572')
ys581 = Real('ys581')
ys582 = Real('ys582')
ys591 = Real('ys591')
ys592 = Real('ys592')
ys601 = Real('ys601')
ys602 = Real('ys602')
ys611 = Real('ys611')
ys612 = Real('ys612')
ys621 = Real('ys621')
ys622 = Real('ys622')
ys631 = Real('ys631')
ys632 = Real('ys632')
ys641 = Real('ys641')
ys642 = Real('ys642')
ys651 = Real('ys651')
ys652 = Real('ys652')
ys661 = Real('ys661')
ys662 = Real('ys662')
ys671 = Real('ys671')
ys672 = Real('ys672')
ys681 = Real('ys681')
ys682 = Real('ys682')
ys691 = Real('ys691')
ys692 = Real('ys692')
ys701 = Real('ys701')
ys702 = Real('ys702')
ys711 = Real('ys711')
ys712 = Real('ys712')
ys721 = Real('ys721')
ys722 = Real('ys722')
ys731 = Real('ys731')
ys732 = Real('ys732')
ys741 = Real('ys741')
ys742 = Real('ys742')
ys751 = Real('ys751')
ys752 = Real('ys752')
ys761 = Real('ys761')
ys762 = Real('ys762')
ys771 = Real('ys771')
ys772 = Real('ys772')
ys781 = Real('ys781')
ys782 = Real('ys782')
ys791 = Real('ys791')
ys792 = Real('ys792')
ys801 = Real('ys801')
ys802 = Real('ys802')
ys811 = Real('ys811')
ys812 = Real('ys812')
ys821 = Real('ys821')
ys822 = Real('ys822')
ys831 = Real('ys831')
ys832 = Real('ys832')
ys841 = Real('ys841')
ys842 = Real('ys842')
ys851 = Real('ys851')
ys852 = Real('ys852')
ys861 = Real('ys861')
ys862 = Real('ys862')
ys871 = Real('ys871')
ys872 = Real('ys872')
ys881 = Real('ys881')
ys882 = Real('ys882')
ys891 = Real('ys891')
ys892 = Real('ys892')
ys901 = Real('ys901')
ys902 = Real('ys902')
ys911 = Real('ys911')
ys912 = Real('ys912')
ys921 = Real('ys921')
ys922 = Real('ys922')
ys931 = Real('ys931')
ys932 = Real('ys932')
ys941 = Real('ys941')
ys942 = Real('ys942')
ys951 = Real('ys951')
ys952 = Real('ys952')
ys961 = Real('ys961')
ys962 = Real('ys962')
ys971 = Real('ys971')
ys972 = Real('ys972')
ys981 = Real('ys981')
ys982 = Real('ys982')
ys991 = Real('ys991')
ys992 = Real('ys992')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=2, pi1>=1, pi2>=0, pi3>=1, pi4>=2, pi5>=3, pi6>=4, pi7>=5, pi8>=6, pi9>=7, pi10>=8, pi11>=9, pi12>=10, pi13>=11, pi14>=12, pi15>=13, pi16>=14, pi17>=15, pi18>=16, pi19>=17, pi20>=18, pi21>=19, pi22>=20, pi23>=21, pi24>=22, pi25>=23, pi26>=24, pi27>=25, pi28>=26, pi29>=27, pi30>=28, pi31>=29, pi32>=30, pi33>=31, pi34>=32, pi35>=33, pi36>=34, pi37>=35, pi38>=36, pi39>=37, pi40>=38, pi41>=39, pi42>=40, pi43>=41, pi44>=42, pi45>=43, pi46>=44, pi47>=45, pi48>=46, pi49>=47, pi50>=48, pi51>=49, pi52>=50, pi53>=51, pi54>=52, pi55>=53, pi56>=54, pi57>=55, pi58>=56, pi59>=57, pi60>=58, pi61>=59, pi62>=60, pi63>=61, pi64>=62, pi65>=63, pi66>=64, pi67>=65, pi68>=66, pi69>=67, pi70>=68, pi71>=69, pi72>=70, pi73>=71, pi74>=72, pi75>=73, pi76>=74, pi77>=75, pi78>=76, pi79>=77, pi80>=78, pi81>=79, pi82>=80, pi83>=81, pi84>=82, pi85>=83, pi86>=84, pi87>=85, pi88>=86, pi89>=87, pi90>=88, pi91>=89, pi92>=90, pi93>=91, pi94>=92, pi95>=93, pi96>=94, pi97>=95, pi98>=96, pi99>=97, 
# Expected cost/reard equations
pi0 == (ys01*xo1l+ ys02*xo2l)*(1 + pi0) + (ys01*xo1r+ ys02*xo2r)*(1 + pi1),
pi1 == (ys11*xo1l+ ys12*xo2l)*(1 + pi0) + (ys11*xo1r+ ys12*xo2r)*(1 + pi2),
pi2 == 0, 
pi3 == (ys31*xo1l+ ys32*xo2l)*(1 + pi2) + (ys31*xo1r+ ys32*xo2r)*(1 + pi4),
pi4 == (ys41*xo1l+ ys42*xo2l)*(1 + pi3) + (ys41*xo1r+ ys42*xo2r)*(1 + pi5),
pi5 == (ys51*xo1l+ ys52*xo2l)*(1 + pi4) + (ys51*xo1r+ ys52*xo2r)*(1 + pi6),
pi6 == (ys61*xo1l+ ys62*xo2l)*(1 + pi5) + (ys61*xo1r+ ys62*xo2r)*(1 + pi7),
pi7 == (ys71*xo1l+ ys72*xo2l)*(1 + pi6) + (ys71*xo1r+ ys72*xo2r)*(1 + pi8),
pi8 == (ys81*xo1l+ ys82*xo2l)*(1 + pi7) + (ys81*xo1r+ ys82*xo2r)*(1 + pi9),
pi9 == (ys91*xo1l+ ys92*xo2l)*(1 + pi8) + (ys91*xo1r+ ys92*xo2r)*(1 + pi10),
pi10 == (ys101*xo1l+ ys102*xo2l)*(1 + pi9) + (ys101*xo1r+ ys102*xo2r)*(1 + pi11),
pi11 == (ys111*xo1l+ ys112*xo2l)*(1 + pi10) + (ys111*xo1r+ ys112*xo2r)*(1 + pi12),
pi12 == (ys121*xo1l+ ys122*xo2l)*(1 + pi11) + (ys121*xo1r+ ys122*xo2r)*(1 + pi13),
pi13 == (ys131*xo1l+ ys132*xo2l)*(1 + pi12) + (ys131*xo1r+ ys132*xo2r)*(1 + pi14),
pi14 == (ys141*xo1l+ ys142*xo2l)*(1 + pi13) + (ys141*xo1r+ ys142*xo2r)*(1 + pi15),
pi15 == (ys151*xo1l+ ys152*xo2l)*(1 + pi14) + (ys151*xo1r+ ys152*xo2r)*(1 + pi16),
pi16 == (ys161*xo1l+ ys162*xo2l)*(1 + pi15) + (ys161*xo1r+ ys162*xo2r)*(1 + pi17),
pi17 == (ys171*xo1l+ ys172*xo2l)*(1 + pi16) + (ys171*xo1r+ ys172*xo2r)*(1 + pi18),
pi18 == (ys181*xo1l+ ys182*xo2l)*(1 + pi17) + (ys181*xo1r+ ys182*xo2r)*(1 + pi19),
pi19 == (ys191*xo1l+ ys192*xo2l)*(1 + pi18) + (ys191*xo1r+ ys192*xo2r)*(1 + pi20),
pi20 == (ys201*xo1l+ ys202*xo2l)*(1 + pi19) + (ys201*xo1r+ ys202*xo2r)*(1 + pi21),
pi21 == (ys211*xo1l+ ys212*xo2l)*(1 + pi20) + (ys211*xo1r+ ys212*xo2r)*(1 + pi22),
pi22 == (ys221*xo1l+ ys222*xo2l)*(1 + pi21) + (ys221*xo1r+ ys222*xo2r)*(1 + pi23),
pi23 == (ys231*xo1l+ ys232*xo2l)*(1 + pi22) + (ys231*xo1r+ ys232*xo2r)*(1 + pi24),
pi24 == (ys241*xo1l+ ys242*xo2l)*(1 + pi23) + (ys241*xo1r+ ys242*xo2r)*(1 + pi25),
pi25 == (ys251*xo1l+ ys252*xo2l)*(1 + pi24) + (ys251*xo1r+ ys252*xo2r)*(1 + pi26),
pi26 == (ys261*xo1l+ ys262*xo2l)*(1 + pi25) + (ys261*xo1r+ ys262*xo2r)*(1 + pi27),
pi27 == (ys271*xo1l+ ys272*xo2l)*(1 + pi26) + (ys271*xo1r+ ys272*xo2r)*(1 + pi28),
pi28 == (ys281*xo1l+ ys282*xo2l)*(1 + pi27) + (ys281*xo1r+ ys282*xo2r)*(1 + pi29),
pi29 == (ys291*xo1l+ ys292*xo2l)*(1 + pi28) + (ys291*xo1r+ ys292*xo2r)*(1 + pi30),
pi30 == (ys301*xo1l+ ys302*xo2l)*(1 + pi29) + (ys301*xo1r+ ys302*xo2r)*(1 + pi31),
pi31 == (ys311*xo1l+ ys312*xo2l)*(1 + pi30) + (ys311*xo1r+ ys312*xo2r)*(1 + pi32),
pi32 == (ys321*xo1l+ ys322*xo2l)*(1 + pi31) + (ys321*xo1r+ ys322*xo2r)*(1 + pi33),
pi33 == (ys331*xo1l+ ys332*xo2l)*(1 + pi32) + (ys331*xo1r+ ys332*xo2r)*(1 + pi34),
pi34 == (ys341*xo1l+ ys342*xo2l)*(1 + pi33) + (ys341*xo1r+ ys342*xo2r)*(1 + pi35),
pi35 == (ys351*xo1l+ ys352*xo2l)*(1 + pi34) + (ys351*xo1r+ ys352*xo2r)*(1 + pi36),
pi36 == (ys361*xo1l+ ys362*xo2l)*(1 + pi35) + (ys361*xo1r+ ys362*xo2r)*(1 + pi37),
pi37 == (ys371*xo1l+ ys372*xo2l)*(1 + pi36) + (ys371*xo1r+ ys372*xo2r)*(1 + pi38),
pi38 == (ys381*xo1l+ ys382*xo2l)*(1 + pi37) + (ys381*xo1r+ ys382*xo2r)*(1 + pi39),
pi39 == (ys391*xo1l+ ys392*xo2l)*(1 + pi38) + (ys391*xo1r+ ys392*xo2r)*(1 + pi40),
pi40 == (ys401*xo1l+ ys402*xo2l)*(1 + pi39) + (ys401*xo1r+ ys402*xo2r)*(1 + pi41),
pi41 == (ys411*xo1l+ ys412*xo2l)*(1 + pi40) + (ys411*xo1r+ ys412*xo2r)*(1 + pi42),
pi42 == (ys421*xo1l+ ys422*xo2l)*(1 + pi41) + (ys421*xo1r+ ys422*xo2r)*(1 + pi43),
pi43 == (ys431*xo1l+ ys432*xo2l)*(1 + pi42) + (ys431*xo1r+ ys432*xo2r)*(1 + pi44),
pi44 == (ys441*xo1l+ ys442*xo2l)*(1 + pi43) + (ys441*xo1r+ ys442*xo2r)*(1 + pi45),
pi45 == (ys451*xo1l+ ys452*xo2l)*(1 + pi44) + (ys451*xo1r+ ys452*xo2r)*(1 + pi46),
pi46 == (ys461*xo1l+ ys462*xo2l)*(1 + pi45) + (ys461*xo1r+ ys462*xo2r)*(1 + pi47),
pi47 == (ys471*xo1l+ ys472*xo2l)*(1 + pi46) + (ys471*xo1r+ ys472*xo2r)*(1 + pi48),
pi48 == (ys481*xo1l+ ys482*xo2l)*(1 + pi47) + (ys481*xo1r+ ys482*xo2r)*(1 + pi49),
pi49 == (ys491*xo1l+ ys492*xo2l)*(1 + pi48) + (ys491*xo1r+ ys492*xo2r)*(1 + pi50),
pi50 == (ys501*xo1l+ ys502*xo2l)*(1 + pi49) + (ys501*xo1r+ ys502*xo2r)*(1 + pi51),
pi51 == (ys511*xo1l+ ys512*xo2l)*(1 + pi50) + (ys511*xo1r+ ys512*xo2r)*(1 + pi52),
pi52 == (ys521*xo1l+ ys522*xo2l)*(1 + pi51) + (ys521*xo1r+ ys522*xo2r)*(1 + pi53),
pi53 == (ys531*xo1l+ ys532*xo2l)*(1 + pi52) + (ys531*xo1r+ ys532*xo2r)*(1 + pi54),
pi54 == (ys541*xo1l+ ys542*xo2l)*(1 + pi53) + (ys541*xo1r+ ys542*xo2r)*(1 + pi55),
pi55 == (ys551*xo1l+ ys552*xo2l)*(1 + pi54) + (ys551*xo1r+ ys552*xo2r)*(1 + pi56),
pi56 == (ys561*xo1l+ ys562*xo2l)*(1 + pi55) + (ys561*xo1r+ ys562*xo2r)*(1 + pi57),
pi57 == (ys571*xo1l+ ys572*xo2l)*(1 + pi56) + (ys571*xo1r+ ys572*xo2r)*(1 + pi58),
pi58 == (ys581*xo1l+ ys582*xo2l)*(1 + pi57) + (ys581*xo1r+ ys582*xo2r)*(1 + pi59),
pi59 == (ys591*xo1l+ ys592*xo2l)*(1 + pi58) + (ys591*xo1r+ ys592*xo2r)*(1 + pi60),
pi60 == (ys601*xo1l+ ys602*xo2l)*(1 + pi59) + (ys601*xo1r+ ys602*xo2r)*(1 + pi61),
pi61 == (ys611*xo1l+ ys612*xo2l)*(1 + pi60) + (ys611*xo1r+ ys612*xo2r)*(1 + pi62),
pi62 == (ys621*xo1l+ ys622*xo2l)*(1 + pi61) + (ys621*xo1r+ ys622*xo2r)*(1 + pi63),
pi63 == (ys631*xo1l+ ys632*xo2l)*(1 + pi62) + (ys631*xo1r+ ys632*xo2r)*(1 + pi64),
pi64 == (ys641*xo1l+ ys642*xo2l)*(1 + pi63) + (ys641*xo1r+ ys642*xo2r)*(1 + pi65),
pi65 == (ys651*xo1l+ ys652*xo2l)*(1 + pi64) + (ys651*xo1r+ ys652*xo2r)*(1 + pi66),
pi66 == (ys661*xo1l+ ys662*xo2l)*(1 + pi65) + (ys661*xo1r+ ys662*xo2r)*(1 + pi67),
pi67 == (ys671*xo1l+ ys672*xo2l)*(1 + pi66) + (ys671*xo1r+ ys672*xo2r)*(1 + pi68),
pi68 == (ys681*xo1l+ ys682*xo2l)*(1 + pi67) + (ys681*xo1r+ ys682*xo2r)*(1 + pi69),
pi69 == (ys691*xo1l+ ys692*xo2l)*(1 + pi68) + (ys691*xo1r+ ys692*xo2r)*(1 + pi70),
pi70 == (ys701*xo1l+ ys702*xo2l)*(1 + pi69) + (ys701*xo1r+ ys702*xo2r)*(1 + pi71),
pi71 == (ys711*xo1l+ ys712*xo2l)*(1 + pi70) + (ys711*xo1r+ ys712*xo2r)*(1 + pi72),
pi72 == (ys721*xo1l+ ys722*xo2l)*(1 + pi71) + (ys721*xo1r+ ys722*xo2r)*(1 + pi73),
pi73 == (ys731*xo1l+ ys732*xo2l)*(1 + pi72) + (ys731*xo1r+ ys732*xo2r)*(1 + pi74),
pi74 == (ys741*xo1l+ ys742*xo2l)*(1 + pi73) + (ys741*xo1r+ ys742*xo2r)*(1 + pi75),
pi75 == (ys751*xo1l+ ys752*xo2l)*(1 + pi74) + (ys751*xo1r+ ys752*xo2r)*(1 + pi76),
pi76 == (ys761*xo1l+ ys762*xo2l)*(1 + pi75) + (ys761*xo1r+ ys762*xo2r)*(1 + pi77),
pi77 == (ys771*xo1l+ ys772*xo2l)*(1 + pi76) + (ys771*xo1r+ ys772*xo2r)*(1 + pi78),
pi78 == (ys781*xo1l+ ys782*xo2l)*(1 + pi77) + (ys781*xo1r+ ys782*xo2r)*(1 + pi79),
pi79 == (ys791*xo1l+ ys792*xo2l)*(1 + pi78) + (ys791*xo1r+ ys792*xo2r)*(1 + pi80),
pi80 == (ys801*xo1l+ ys802*xo2l)*(1 + pi79) + (ys801*xo1r+ ys802*xo2r)*(1 + pi81),
pi81 == (ys811*xo1l+ ys812*xo2l)*(1 + pi80) + (ys811*xo1r+ ys812*xo2r)*(1 + pi82),
pi82 == (ys821*xo1l+ ys822*xo2l)*(1 + pi81) + (ys821*xo1r+ ys822*xo2r)*(1 + pi83),
pi83 == (ys831*xo1l+ ys832*xo2l)*(1 + pi82) + (ys831*xo1r+ ys832*xo2r)*(1 + pi84),
pi84 == (ys841*xo1l+ ys842*xo2l)*(1 + pi83) + (ys841*xo1r+ ys842*xo2r)*(1 + pi85),
pi85 == (ys851*xo1l+ ys852*xo2l)*(1 + pi84) + (ys851*xo1r+ ys852*xo2r)*(1 + pi86),
pi86 == (ys861*xo1l+ ys862*xo2l)*(1 + pi85) + (ys861*xo1r+ ys862*xo2r)*(1 + pi87),
pi87 == (ys871*xo1l+ ys872*xo2l)*(1 + pi86) + (ys871*xo1r+ ys872*xo2r)*(1 + pi88),
pi88 == (ys881*xo1l+ ys882*xo2l)*(1 + pi87) + (ys881*xo1r+ ys882*xo2r)*(1 + pi89),
pi89 == (ys891*xo1l+ ys892*xo2l)*(1 + pi88) + (ys891*xo1r+ ys892*xo2r)*(1 + pi90),
pi90 == (ys901*xo1l+ ys902*xo2l)*(1 + pi89) + (ys901*xo1r+ ys902*xo2r)*(1 + pi91),
pi91 == (ys911*xo1l+ ys912*xo2l)*(1 + pi90) + (ys911*xo1r+ ys912*xo2r)*(1 + pi92),
pi92 == (ys921*xo1l+ ys922*xo2l)*(1 + pi91) + (ys921*xo1r+ ys922*xo2r)*(1 + pi93),
pi93 == (ys931*xo1l+ ys932*xo2l)*(1 + pi92) + (ys931*xo1r+ ys932*xo2r)*(1 + pi94),
pi94 == (ys941*xo1l+ ys942*xo2l)*(1 + pi93) + (ys941*xo1r+ ys942*xo2r)*(1 + pi95),
pi95 == (ys951*xo1l+ ys952*xo2l)*(1 + pi94) + (ys951*xo1r+ ys952*xo2r)*(1 + pi96),
pi96 == (ys961*xo1l+ ys962*xo2l)*(1 + pi95) + (ys961*xo1r+ ys962*xo2r)*(1 + pi97),
pi97 == (ys971*xo1l+ ys972*xo2l)*(1 + pi96) + (ys971*xo1r+ ys972*xo2r)*(1 + pi98),
pi98 == (ys981*xo1l+ ys982*xo2l)*(1 + pi97) + (ys981*xo1r+ ys982*xo2r)*(1 + pi99),
pi99 == (ys991*xo1l+ ys992*xo2l)*(1 + pi98) + (ys991*xo1r+ ys992*xo2r)*(1 + pi99),
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= 1.5
(pi0+pi1+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi30+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47+pi48+pi49+pi50+pi51+pi52+pi53+pi54+pi55+pi56+pi57+pi58+pi59+pi60+pi61+pi62+pi63+pi64+pi65+pi66+pi67+pi68+pi69+pi70+pi71+pi72+pi73+pi74+pi75+pi76+pi77+pi78+pi79+pi80+pi81+pi82+pi83+pi84+pi85+pi86+pi87+pi88+pi89+pi90+pi91+pi92+pi93+pi94+pi95+pi96+pi97+pi98+pi99) * Q(1,99) <= 1.5,
# Randomised strategies (proper probability distributions)
xo1l>= 0,
xo1l<= 1,
xo1r>= 0,
xo1r<= 1,
xo2l>= 0,
xo2l<= 1,
xo2r>= 0,
xo2r<= 1,
xo1l + xo1r == 1,
xo2l + xo2r == 1,
# ysNM is a function that should map every state N to some observable class M
Or(ys01== 0 , ys01== 1),
Or(ys02== 0 , ys02== 1),
Or(ys11== 0 , ys11== 1),
Or(ys12== 0 , ys12== 1),
Or(ys31== 0 , ys31== 1),
Or(ys32== 0 , ys32== 1),
Or(ys41== 0 , ys41== 1),
Or(ys42== 0 , ys42== 1),
Or(ys51== 0 , ys51== 1),
Or(ys52== 0 , ys52== 1),
Or(ys61== 0 , ys61== 1),
Or(ys62== 0 , ys62== 1),
Or(ys71== 0 , ys71== 1),
Or(ys72== 0 , ys72== 1),
Or(ys81== 0 , ys81== 1),
Or(ys82== 0 , ys82== 1),
Or(ys91== 0 , ys91== 1),
Or(ys92== 0 , ys92== 1),
Or(ys101== 0 , ys101== 1),
Or(ys102== 0 , ys102== 1),
Or(ys111== 0 , ys111== 1),
Or(ys112== 0 , ys112== 1),
Or(ys121== 0 , ys121== 1),
Or(ys122== 0 , ys122== 1),
Or(ys131== 0 , ys131== 1),
Or(ys132== 0 , ys132== 1),
Or(ys141== 0 , ys141== 1),
Or(ys142== 0 , ys142== 1),
Or(ys151== 0 , ys151== 1),
Or(ys152== 0 , ys152== 1),
Or(ys161== 0 , ys161== 1),
Or(ys162== 0 , ys162== 1),
Or(ys171== 0 , ys171== 1),
Or(ys172== 0 , ys172== 1),
Or(ys181== 0 , ys181== 1),
Or(ys182== 0 , ys182== 1),
Or(ys191== 0 , ys191== 1),
Or(ys192== 0 , ys192== 1),
Or(ys201== 0 , ys201== 1),
Or(ys202== 0 , ys202== 1),
Or(ys211== 0 , ys211== 1),
Or(ys212== 0 , ys212== 1),
Or(ys221== 0 , ys221== 1),
Or(ys222== 0 , ys222== 1),
Or(ys231== 0 , ys231== 1),
Or(ys232== 0 , ys232== 1),
Or(ys241== 0 , ys241== 1),
Or(ys242== 0 , ys242== 1),
Or(ys251== 0 , ys251== 1),
Or(ys252== 0 , ys252== 1),
Or(ys261== 0 , ys261== 1),
Or(ys262== 0 , ys262== 1),
Or(ys271== 0 , ys271== 1),
Or(ys272== 0 , ys272== 1),
Or(ys281== 0 , ys281== 1),
Or(ys282== 0 , ys282== 1),
Or(ys291== 0 , ys291== 1),
Or(ys292== 0 , ys292== 1),
Or(ys301== 0 , ys301== 1),
Or(ys302== 0 , ys302== 1),
Or(ys311== 0 , ys311== 1),
Or(ys312== 0 , ys312== 1),
Or(ys321== 0 , ys321== 1),
Or(ys322== 0 , ys322== 1),
Or(ys331== 0 , ys331== 1),
Or(ys332== 0 , ys332== 1),
Or(ys341== 0 , ys341== 1),
Or(ys342== 0 , ys342== 1),
Or(ys351== 0 , ys351== 1),
Or(ys352== 0 , ys352== 1),
Or(ys361== 0 , ys361== 1),
Or(ys362== 0 , ys362== 1),
Or(ys371== 0 , ys371== 1),
Or(ys372== 0 , ys372== 1),
Or(ys381== 0 , ys381== 1),
Or(ys382== 0 , ys382== 1),
Or(ys391== 0 , ys391== 1),
Or(ys392== 0 , ys392== 1),
Or(ys401== 0 , ys401== 1),
Or(ys402== 0 , ys402== 1),
Or(ys411== 0 , ys411== 1),
Or(ys412== 0 , ys412== 1),
Or(ys421== 0 , ys421== 1),
Or(ys422== 0 , ys422== 1),
Or(ys431== 0 , ys431== 1),
Or(ys432== 0 , ys432== 1),
Or(ys441== 0 , ys441== 1),
Or(ys442== 0 , ys442== 1),
Or(ys451== 0 , ys451== 1),
Or(ys452== 0 , ys452== 1),
Or(ys461== 0 , ys461== 1),
Or(ys462== 0 , ys462== 1),
Or(ys471== 0 , ys471== 1),
Or(ys472== 0 , ys472== 1),
Or(ys481== 0 , ys481== 1),
Or(ys482== 0 , ys482== 1),
Or(ys491== 0 , ys491== 1),
Or(ys492== 0 , ys492== 1),
Or(ys501== 0 , ys501== 1),
Or(ys502== 0 , ys502== 1),
Or(ys511== 0 , ys511== 1),
Or(ys512== 0 , ys512== 1),
Or(ys521== 0 , ys521== 1),
Or(ys522== 0 , ys522== 1),
Or(ys531== 0 , ys531== 1),
Or(ys532== 0 , ys532== 1),
Or(ys541== 0 , ys541== 1),
Or(ys542== 0 , ys542== 1),
Or(ys551== 0 , ys551== 1),
Or(ys552== 0 , ys552== 1),
Or(ys561== 0 , ys561== 1),
Or(ys562== 0 , ys562== 1),
Or(ys571== 0 , ys571== 1),
Or(ys572== 0 , ys572== 1),
Or(ys581== 0 , ys581== 1),
Or(ys582== 0 , ys582== 1),
Or(ys591== 0 , ys591== 1),
Or(ys592== 0 , ys592== 1),
Or(ys601== 0 , ys601== 1),
Or(ys602== 0 , ys602== 1),
Or(ys611== 0 , ys611== 1),
Or(ys612== 0 , ys612== 1),
Or(ys621== 0 , ys621== 1),
Or(ys622== 0 , ys622== 1),
Or(ys631== 0 , ys631== 1),
Or(ys632== 0 , ys632== 1),
Or(ys641== 0 , ys641== 1),
Or(ys642== 0 , ys642== 1),
Or(ys651== 0 , ys651== 1),
Or(ys652== 0 , ys652== 1),
Or(ys661== 0 , ys661== 1),
Or(ys662== 0 , ys662== 1),
Or(ys671== 0 , ys671== 1),
Or(ys672== 0 , ys672== 1),
Or(ys681== 0 , ys681== 1),
Or(ys682== 0 , ys682== 1),
Or(ys691== 0 , ys691== 1),
Or(ys692== 0 , ys692== 1),
Or(ys701== 0 , ys701== 1),
Or(ys702== 0 , ys702== 1),
Or(ys711== 0 , ys711== 1),
Or(ys712== 0 , ys712== 1),
Or(ys721== 0 , ys721== 1),
Or(ys722== 0 , ys722== 1),
Or(ys731== 0 , ys731== 1),
Or(ys732== 0 , ys732== 1),
Or(ys741== 0 , ys741== 1),
Or(ys742== 0 , ys742== 1),
Or(ys751== 0 , ys751== 1),
Or(ys752== 0 , ys752== 1),
Or(ys761== 0 , ys761== 1),
Or(ys762== 0 , ys762== 1),
Or(ys771== 0 , ys771== 1),
Or(ys772== 0 , ys772== 1),
Or(ys781== 0 , ys781== 1),
Or(ys782== 0 , ys782== 1),
Or(ys791== 0 , ys791== 1),
Or(ys792== 0 , ys792== 1),
Or(ys801== 0 , ys801== 1),
Or(ys802== 0 , ys802== 1),
Or(ys811== 0 , ys811== 1),
Or(ys812== 0 , ys812== 1),
Or(ys821== 0 , ys821== 1),
Or(ys822== 0 , ys822== 1),
Or(ys831== 0 , ys831== 1),
Or(ys832== 0 , ys832== 1),
Or(ys841== 0 , ys841== 1),
Or(ys842== 0 , ys842== 1),
Or(ys851== 0 , ys851== 1),
Or(ys852== 0 , ys852== 1),
Or(ys861== 0 , ys861== 1),
Or(ys862== 0 , ys862== 1),
Or(ys871== 0 , ys871== 1),
Or(ys872== 0 , ys872== 1),
Or(ys881== 0 , ys881== 1),
Or(ys882== 0 , ys882== 1),
Or(ys891== 0 , ys891== 1),
Or(ys892== 0 , ys892== 1),
Or(ys901== 0 , ys901== 1),
Or(ys902== 0 , ys902== 1),
Or(ys911== 0 , ys911== 1),
Or(ys912== 0 , ys912== 1),
Or(ys921== 0 , ys921== 1),
Or(ys922== 0 , ys922== 1),
Or(ys931== 0 , ys931== 1),
Or(ys932== 0 , ys932== 1),
Or(ys941== 0 , ys941== 1),
Or(ys942== 0 , ys942== 1),
Or(ys951== 0 , ys951== 1),
Or(ys952== 0 , ys952== 1),
Or(ys961== 0 , ys961== 1),
Or(ys962== 0 , ys962== 1),
Or(ys971== 0 , ys971== 1),
Or(ys972== 0 , ys972== 1),
Or(ys981== 0 , ys981== 1),
Or(ys982== 0 , ys982== 1),
Or(ys991== 0 , ys991== 1),
Or(ys992== 0 , ys992== 1),
# Every state should be mapped to exactly one equivalence class
ys01 + ys02 == 1,
ys11 + ys12 == 1,
ys31 + ys32 == 1,
ys41 + ys42 == 1,
ys51 + ys52 == 1,
ys61 + ys62 == 1,
ys71 + ys72 == 1,
ys81 + ys82 == 1,
ys91 + ys92 == 1,
ys101 + ys102 == 1,
ys111 + ys112 == 1,
ys121 + ys122 == 1,
ys131 + ys132 == 1,
ys141 + ys142 == 1,
ys151 + ys152 == 1,
ys161 + ys162 == 1,
ys171 + ys172 == 1,
ys181 + ys182 == 1,
ys191 + ys192 == 1,
ys201 + ys202 == 1,
ys211 + ys212 == 1,
ys221 + ys222 == 1,
ys231 + ys232 == 1,
ys241 + ys242 == 1,
ys251 + ys252 == 1,
ys261 + ys262 == 1,
ys271 + ys272 == 1,
ys281 + ys282 == 1,
ys291 + ys292 == 1,
ys301 + ys302 == 1,
ys311 + ys312 == 1,
ys321 + ys322 == 1,
ys331 + ys332 == 1,
ys341 + ys342 == 1,
ys351 + ys352 == 1,
ys361 + ys362 == 1,
ys371 + ys372 == 1,
ys381 + ys382 == 1,
ys391 + ys392 == 1,
ys401 + ys402 == 1,
ys411 + ys412 == 1,
ys421 + ys422 == 1,
ys431 + ys432 == 1,
ys441 + ys442 == 1,
ys451 + ys452 == 1,
ys461 + ys462 == 1,
ys471 + ys472 == 1,
ys481 + ys482 == 1,
ys491 + ys492 == 1,
ys501 + ys502 == 1,
ys511 + ys512 == 1,
ys521 + ys522 == 1,
ys531 + ys532 == 1,
ys541 + ys542 == 1,
ys551 + ys552 == 1,
ys561 + ys562 == 1,
ys571 + ys572 == 1,
ys581 + ys582 == 1,
ys591 + ys592 == 1,
ys601 + ys602 == 1,
ys611 + ys612 == 1,
ys621 + ys622 == 1,
ys631 + ys632 == 1,
ys641 + ys642 == 1,
ys651 + ys652 == 1,
ys661 + ys662 == 1,
ys671 + ys672 == 1,
ys681 + ys682 == 1,
ys691 + ys692 == 1,
ys701 + ys702 == 1,
ys711 + ys712 == 1,
ys721 + ys722 == 1,
ys731 + ys732 == 1,
ys741 + ys742 == 1,
ys751 + ys752 == 1,
ys761 + ys762 == 1,
ys771 + ys772 == 1,
ys781 + ys782 == 1,
ys791 + ys792 == 1,
ys801 + ys802 == 1,
ys811 + ys812 == 1,
ys821 + ys822 == 1,
ys831 + ys832 == 1,
ys841 + ys842 == 1,
ys851 + ys852 == 1,
ys861 + ys862 == 1,
ys871 + ys872 == 1,
ys881 + ys882 == 1,
ys891 + ys892 == 1,
ys901 + ys902 == 1,
ys911 + ys912 == 1,
ys921 + ys922 == 1,
ys931 + ys932 == 1,
ys941 + ys942 == 1,
ys951 + ys952 == 1,
ys961 + ys962 == 1,
ys971 + ys972 == 1,
ys981 + ys982 == 1,
ys991 + ys992 == 1
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
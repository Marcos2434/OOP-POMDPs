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
pi0>=2, pi1>=1, pi2>=0, pi3>=1, pi4>=2, pi5>=2, pi6>=1, pi7>=1, pi8>=2, pi9>=3, pi10>=3, pi11>=2, pi12>=2, pi13>=3, pi14>=4, pi15>=4, pi16>=3, pi17>=3, pi18>=4, pi19>=5, pi20>=5, pi21>=4, pi22>=4, pi23>=5, pi24>=6, 
# Expected cost/reard equations
pi0 == (ys01*xo1l + ys02*xo2l) * (1 + pi0) + (ys01*xo1r + ys02*xo2r) * (1 + pi1) + (ys01*xo1u + ys02*xo2u) * (1 + pi0) + (ys01*xo1d + ys02*xo2d) * (1 + pi5),
pi1 == (ys11*xo1l + ys12*xo2l) * (1 + pi0) + (ys11*xo1r + ys12*xo2r) * (1 + pi2) + (ys11*xo1u + ys12*xo2u) * (1 + pi1) + (ys11*xo1d + ys12*xo2d) * (1 + pi6),
pi2 == 0, 
pi3 == (ys31*xo1l + ys32*xo2l) * (1 + pi2) + (ys31*xo1r + ys32*xo2r) * (1 + pi4) + (ys31*xo1u + ys32*xo2u) * (1 + pi3) + (ys31*xo1d + ys32*xo2d) * (1 + pi8),
pi4 == (ys41*xo1l + ys42*xo2l) * (1 + pi3) + (ys41*xo1r + ys42*xo2r) * (1 + pi4) + (ys41*xo1u + ys42*xo2u) * (1 + pi4) + (ys41*xo1d + ys42*xo2d) * (1 + pi9),
pi5 == (ys51*xo1l + ys52*xo2l) * (1 + pi5) + (ys51*xo1r + ys52*xo2r) * (1 + pi6) + (ys51*xo1u + ys52*xo2u) * (1 + pi0) + (ys51*xo1d + ys52*xo2d) * (1 + pi10),
pi6 == (ys61*xo1l + ys62*xo2l) * (1 + pi5) + (ys61*xo1r + ys62*xo2r) * (1 + pi7) + (ys61*xo1u + ys62*xo2u) * (1 + pi1) + (ys61*xo1d + ys62*xo2d) * (1 + pi11),
pi7 == (ys71*xo1l + ys72*xo2l) * (1 + pi6) + (ys71*xo1r + ys72*xo2r) * (1 + pi8) + (ys71*xo1u + ys72*xo2u) * (1 + pi2) + (ys71*xo1d + ys72*xo2d) * (1 + pi12),
pi8 == (ys81*xo1l + ys82*xo2l) * (1 + pi7) + (ys81*xo1r + ys82*xo2r) * (1 + pi9) + (ys81*xo1u + ys82*xo2u) * (1 + pi3) + (ys81*xo1d + ys82*xo2d) * (1 + pi13),
pi9 == (ys91*xo1l + ys92*xo2l) * (1 + pi8) + (ys91*xo1r + ys92*xo2r) * (1 + pi9) + (ys91*xo1u + ys92*xo2u) * (1 + pi4) + (ys91*xo1d + ys92*xo2d) * (1 + pi14),
pi10 == (ys101*xo1l + ys102*xo2l) * (1 + pi10) + (ys101*xo1r + ys102*xo2r) * (1 + pi11) + (ys101*xo1u + ys102*xo2u) * (1 + pi5) + (ys101*xo1d + ys102*xo2d) * (1 + pi15),
pi11 == (ys111*xo1l + ys112*xo2l) * (1 + pi10) + (ys111*xo1r + ys112*xo2r) * (1 + pi12) + (ys111*xo1u + ys112*xo2u) * (1 + pi6) + (ys111*xo1d + ys112*xo2d) * (1 + pi16),
pi12 == (ys121*xo1l + ys122*xo2l) * (1 + pi11) + (ys121*xo1r + ys122*xo2r) * (1 + pi13) + (ys121*xo1u + ys122*xo2u) * (1 + pi7) + (ys121*xo1d + ys122*xo2d) * (1 + pi17),
pi13 == (ys131*xo1l + ys132*xo2l) * (1 + pi12) + (ys131*xo1r + ys132*xo2r) * (1 + pi14) + (ys131*xo1u + ys132*xo2u) * (1 + pi8) + (ys131*xo1d + ys132*xo2d) * (1 + pi18),
pi14 == (ys141*xo1l + ys142*xo2l) * (1 + pi13) + (ys141*xo1r + ys142*xo2r) * (1 + pi14) + (ys141*xo1u + ys142*xo2u) * (1 + pi9) + (ys141*xo1d + ys142*xo2d) * (1 + pi19),
pi15 == (ys151*xo1l + ys152*xo2l) * (1 + pi15) + (ys151*xo1r + ys152*xo2r) * (1 + pi16) + (ys151*xo1u + ys152*xo2u) * (1 + pi10) + (ys151*xo1d + ys152*xo2d) * (1 + pi20),
pi16 == (ys161*xo1l + ys162*xo2l) * (1 + pi15) + (ys161*xo1r + ys162*xo2r) * (1 + pi17) + (ys161*xo1u + ys162*xo2u) * (1 + pi11) + (ys161*xo1d + ys162*xo2d) * (1 + pi21),
pi17 == (ys171*xo1l + ys172*xo2l) * (1 + pi16) + (ys171*xo1r + ys172*xo2r) * (1 + pi18) + (ys171*xo1u + ys172*xo2u) * (1 + pi12) + (ys171*xo1d + ys172*xo2d) * (1 + pi22),
pi18 == (ys181*xo1l + ys182*xo2l) * (1 + pi17) + (ys181*xo1r + ys182*xo2r) * (1 + pi19) + (ys181*xo1u + ys182*xo2u) * (1 + pi13) + (ys181*xo1d + ys182*xo2d) * (1 + pi23),
pi19 == (ys191*xo1l + ys192*xo2l) * (1 + pi18) + (ys191*xo1r + ys192*xo2r) * (1 + pi19) + (ys191*xo1u + ys192*xo2u) * (1 + pi14) + (ys191*xo1d + ys192*xo2d) * (1 + pi24),
pi20 == (ys201*xo1l + ys202*xo2l) * (1 + pi20) + (ys201*xo1r + ys202*xo2r) * (1 + pi21) + (ys201*xo1u + ys202*xo2u) * (1 + pi15) + (ys201*xo1d + ys202*xo2d) * (1 + pi20),
pi21 == (ys211*xo1l + ys212*xo2l) * (1 + pi20) + (ys211*xo1r + ys212*xo2r) * (1 + pi22) + (ys211*xo1u + ys212*xo2u) * (1 + pi16) + (ys211*xo1d + ys212*xo2d) * (1 + pi21),
pi22 == (ys221*xo1l + ys222*xo2l) * (1 + pi21) + (ys221*xo1r + ys222*xo2r) * (1 + pi23) + (ys221*xo1u + ys222*xo2u) * (1 + pi17) + (ys221*xo1d + ys222*xo2d) * (1 + pi22),
pi23 == (ys231*xo1l + ys232*xo2l) * (1 + pi22) + (ys231*xo1r + ys232*xo2r) * (1 + pi24) + (ys231*xo1u + ys232*xo2u) * (1 + pi18) + (ys231*xo1d + ys232*xo2d) * (1 + pi23),
pi24 == (ys241*xo1l + ys242*xo2l) * (1 + pi23) + (ys241*xo1r + ys242*xo2r) * (1 + pi24) + (ys241*xo1u + ys242*xo2u) * (1 + pi19) + (ys241*xo1d + ys242*xo2d) * (1 + pi24),
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= 1.5
(pi0+pi1+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24) * Q(1,24) <= 1.5,
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
ys241 + ys242 == 1
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
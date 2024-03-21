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

# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)
ys01 = Real('ys01')
ys02 = Real('ys02')
ys11 = Real('ys11')
ys12 = Real('ys12')
ys21 = Real('ys21')
ys22 = Real('ys22')
ys31 = Real('ys31')
ys32 = Real('ys32')
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

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=4, pi1>=3, pi2>=2, pi3>=1, pi4>=0, pi5>=1, pi6>=2, pi7>=3, pi8>=4, pi9>=5, pi10>=6, pi11>=7, pi12>=8, pi13>=9, pi14>=10, pi15>=11, pi16>=12, pi17>=13, pi18>=14, pi19>=15, 
# Expected cost/reard equations
pi0 == (ys01*xo1l+ ys02*xo2l)*(1 + pi0) + (ys01*xo1r+ ys02*xo2r)*(1 + pi1),
pi1 == (ys11*xo1l+ ys12*xo2l)*(1 + pi0) + (ys11*xo1r+ ys12*xo2r)*(1 + pi2),
pi2 == (ys21*xo1l+ ys22*xo2l)*(1 + pi1) + (ys21*xo1r+ ys22*xo2r)*(1 + pi3),
pi3 == (ys31*xo1l+ ys32*xo2l)*(1 + pi2) + (ys31*xo1r+ ys32*xo2r)*(1 + pi4),
pi4 == 0, 
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
pi19 == (ys191*xo1l+ ys192*xo2l)*(1 + pi18) + (ys191*xo1r+ ys192*xo2r)*(1 + pi19),
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= 100
(pi0+pi1+pi2+pi3+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19) * Q(1,19) <= 100,
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
Or(ys21== 0 , ys21== 1),
Or(ys22== 0 , ys22== 1),
Or(ys31== 0 , ys31== 1),
Or(ys32== 0 , ys32== 1),
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
# Every state should be mapped to exactly one equivalence class
ys01 + ys02 == 1,
ys11 + ys12 == 1,
ys21 + ys22 == 1,
ys31 + ys32 == 1,
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
ys191 + ys192 == 1
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
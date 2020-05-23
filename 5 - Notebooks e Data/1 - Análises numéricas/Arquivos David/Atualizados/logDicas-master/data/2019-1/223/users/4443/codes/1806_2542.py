from numpy import *
e = array(eval(input("Digite o numero de pessoas q entraram no bus: ")))
s = array(eval(input("Digite o numero de pessoas q sairam no bus: ")))
passageiros = 0
for i in range(len(e)):
	passageiros = passageiros + e[i] - s[i]
print(passageiros)	
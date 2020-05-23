from math import *
x = eval(input("insira o angulo:"))
k = int(input("insira o numero determos da serie:"))
soma = 0
i = 0
final = k - 1
#termo geral = x**(2*i + 1)/(factorial(2*i + 1))
while(k > i ):
	tg = x**(2*i + 1)
	tg1 = (factorial(2*i + 1))
	soma = soma + ((-1)**i * tg)/tg1
	i = i + 1

print(round(soma,10))

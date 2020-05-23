x = float(input("insira o numero:"))
k = int(input("insira o numero de termos:"))
i = 0
soma = 0
from math import *
#termo geral:x**(2*i +1)/factorial(2*i+1)

while(k > i):
	tg =x**(2*i +1)
	tg1 = factorial(2*i+1)
	soma = soma + (tg/tg1)
	i = i + 1
print(round(soma,9))
	
	
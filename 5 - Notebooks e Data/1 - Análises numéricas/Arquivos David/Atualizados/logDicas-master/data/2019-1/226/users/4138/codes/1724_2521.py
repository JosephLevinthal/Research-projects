n = int(input("insira o numero:"))
soma = 0
i = 0
from math import *
#termpo geral factorial(i) * factorial(2*i)/factorial(i+1) * factorial(2*i+1)
while(n+1 > i):
	tg = factorial(i)
	tg1 = factorial(2*i)
	tg2 = factorial(i+1)
	tg3 =  factorial(2*i+1)
	soma = soma + (tg * tg1)/(tg2 * tg3)
	soma1 = soma 
	print(round(2 * soma1,10))
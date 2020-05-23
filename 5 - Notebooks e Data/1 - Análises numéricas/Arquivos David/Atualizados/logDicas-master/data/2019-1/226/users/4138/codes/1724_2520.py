n = int(input("insira o numero:"))
i = 0
soma = 0
#termo geral (sqrt(6/(i**2)))
from math import *
while(n > i):
	tg = (i +1)**2
	soma = soma + (6/tg)
	soma1 = sqrt(soma)
	i = i + 1
	
print(round(soma1,6))
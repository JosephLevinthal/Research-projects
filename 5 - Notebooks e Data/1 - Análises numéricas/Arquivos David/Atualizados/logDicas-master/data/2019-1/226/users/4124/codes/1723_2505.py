from math import *
x = eval(input("Angulo X: "))
k = int(input("Termos da serie: "))
i = 0
soma = 0
final = k - 1
while(k > i):
	tg = x ** (2*i + 1)	
	tg1 = factorial(2 * i + 1) 
	soma = soma + ((-1)**i * tg)/tg1
	i = i + 1
print(round(soma,10))
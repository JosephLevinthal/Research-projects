from math import *
x = float(input("Numero real: "))
n = int(input("Numero de termos: "))

t = 1

soma = x

while (t < n):
	tg = x**(2*t + 1)/(factorial(2*t+1))
	soma = soma + tg
	t = t + 1
	
print(round(soma,9))
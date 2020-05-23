from math import *
n = int(input("Numero de termos: "))

t = 1

soma = 0

while (t <= n):
	tg = sqrt(12)*((-1)**(t + 1)) / ((2*t - 1)*(3**(t-1)))
	soma = soma + tg
	t = t + 1

print(round(soma,8))

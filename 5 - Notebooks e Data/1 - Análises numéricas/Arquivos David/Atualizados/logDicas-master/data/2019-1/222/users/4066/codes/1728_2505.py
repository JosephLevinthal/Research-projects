from math import *

x = eval(input("Angulo: "))

k = int(input("Numero de termos: "))

soma = 0

t = 0

while (t < k):
	tg = (((-1)**t)/factorial(2*t +1))*x**(2*t +1)
	soma = soma + tg
	t = t + 1

print(round(soma, 10))
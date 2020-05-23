import math

k = int(input("Numero de termos: "))

soma = 0
t = 0

while (t < k):
	tg = 1/(math.factorial(t))
	soma = soma + tg
	t = t+1
	
print(round(soma, 8))
from math import*
a = int(input())
n = 0
f = 2
exp = 0
sinal = 1
acr = 0
while n < a:
	acr += sinal*(1/((f-1)*(3**exp)))
	exp += 1
	sinal = sinal *(-1)
	f += 2
	n += 1
acr = sqrt(12)*acr
print(round(acr,8))	
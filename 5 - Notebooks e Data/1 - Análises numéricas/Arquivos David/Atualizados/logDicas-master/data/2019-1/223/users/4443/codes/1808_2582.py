from math import *
x = float(input("digite um numero real: "))
k = int(input("digite um numero inteiro: "))
cosx = 0
for i in range(k):
	num = x**(2*i)
	den = factorial(2*i)
	parcela = num/den
	cosx = cosx + parcela
print(round(cosx, 8))	
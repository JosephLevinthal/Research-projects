from math import*
x = eval(input("x: "))
k = int(input())
contador = 1
sinal = -1
soma = x
exp = 3
while(contador < k):
	soma = soma + (sinal*(x**exp/factorial(exp)))
	sinal = sinal*(-1)
	exp += 2
	contador += 1

print(round(soma,10))
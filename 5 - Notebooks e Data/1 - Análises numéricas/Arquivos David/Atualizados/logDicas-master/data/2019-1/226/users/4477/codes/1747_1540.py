from math import *
# Entradas
x = eval(input("Determine x: "))
k = int(input("Determine k: "))
# Variavel
soma = 0
i = 0
sinal = -1
# laco
while (x <= k-1):
	soma = soma + sinal * x**i/factorial2 - 1
	sinal = - sinal
	i = i+1
#saida
print(round(soma, 6))
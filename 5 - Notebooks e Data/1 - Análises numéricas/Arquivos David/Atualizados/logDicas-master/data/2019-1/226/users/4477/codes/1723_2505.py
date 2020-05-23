from math import *
#Entradas
x = eval(input("Determine x: "))
k = int(input("Determine k: "))
# Variaveis
soma = 0   # Acumulativa
i = 0      # Contadora
sinal = +1
# Laço
while (i<=k-1):
	soma = soma + sinal * ((x**(2*i+1) / factorial(2*i+1)))
	sinal = - sinal
	i = i + 1
# Saida
print(round(soma, 10))
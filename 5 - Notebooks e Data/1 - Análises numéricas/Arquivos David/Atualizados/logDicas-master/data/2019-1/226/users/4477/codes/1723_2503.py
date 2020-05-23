from math import *
# Entradas
n = int(input("Determine n: "))
# Variaveis
soma = 0               # Acumulativa
i = 0                  # Contadora
sinal = + 1            # Alteração do Sinal
# Laço
while (i <= n-1):
	soma = soma + sinal * 4/(2*i+1)
	sinal = - sinal
	i = i + 1
# Saida
print(round(soma, 8))
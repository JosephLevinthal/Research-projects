from math import *
# Entradas
k = int(input("Determine o numero: "))
# Variaveis
soma = 0     # Acumulativa
i = 0        # Contadora
# Laço
while (i <= k-1):
	soma = soma + 1 / factorial (i)
	i = i + 1
# Saidas
print(round(soma, 8))
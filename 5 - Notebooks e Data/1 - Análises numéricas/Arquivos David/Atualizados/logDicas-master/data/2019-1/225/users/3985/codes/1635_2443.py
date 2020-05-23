# Entradas
from math import*
r = float(input("Raio do tanque: "))
h = float(input("Altura: "))
opcao = float(input("Opcao (1/2)? "))
# Variaveis
V = (4 * pi * r **3)/3
V2 = (pi * h ** 2 * (3 * r - h))/3

if (opcao == 1):
	msg = V2
else:
	msg = V - V2
# Saida
print(round(msg, 4))
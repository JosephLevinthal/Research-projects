from math import *
n = int(input("Digite o numero de pessoas: "))
p_n = 1 - (factorial(365)/factorial(365-n)) * 1 / 365 ** n
porcentagem = p_n * 100
print(round(porcentagem,2))
	
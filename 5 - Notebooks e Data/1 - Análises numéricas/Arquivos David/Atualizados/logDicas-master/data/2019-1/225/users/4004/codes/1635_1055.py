# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

v0 = float(input("velocidade inicial(m/s): "))
alpha = float(input("angulo: "))
D = float(input("distancia horizontal: "))
g = 9.8

alpha = radians(alpha)
den = (v0 ** 2) * sin(2 * alpha)
R = den / g

if abs(D - R) <= 0.1:
	print("sim")
else:
	print("nao")
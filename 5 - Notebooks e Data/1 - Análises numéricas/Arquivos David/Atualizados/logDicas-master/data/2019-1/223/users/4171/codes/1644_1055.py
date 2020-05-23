# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

v0 = float(input("velocidade inicial: "))
a = radians(float(input("angulo: ")))
D = float(input("distancia horizontal: "))

g = 9.8

R = (v0**2 * sin(a + a))/g

if R + 0.1 > D:
	print("sim")
else:
	print("nao")

# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

v = float(input("Velocidade inicial: "))
ang = float(input("Angulo: "))
dist = float(input("A distancia entre eles: "))
x = radians(ang)
r = ((v ** 2) * sin(2 * x)) / 9.8

if abs(dist - r <= 0.1):
	print("sim")
else:
	print("nao")
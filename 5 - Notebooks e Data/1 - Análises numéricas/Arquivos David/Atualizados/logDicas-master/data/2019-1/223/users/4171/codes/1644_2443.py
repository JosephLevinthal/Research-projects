# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

r = float(input("raio do tanque: "))
x = float(input("altura da coluna: "))
n = int(input("volume de ar/combustivel (1 / 2) "))

if n == 1:
	V = (pi * x ** 2 * (r * 3 - x))/3
	print(abs(round(V,4)))
else:
	V = (pi * x ** 2 * (r * 3 - x))/3
	V2 = (4 * pi * r**3)/3
	print(abs(round(V - V2,4)))

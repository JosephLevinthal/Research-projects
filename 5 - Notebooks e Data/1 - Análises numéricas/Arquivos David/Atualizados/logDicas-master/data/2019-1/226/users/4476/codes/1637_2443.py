# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
r = float(input("raio: "))
x = float(input("altura: "))
n = int(input("opcao desejada? (1/2) "))

from math import *
vt = (4*pi*(r**3)) / 3

va = (pi*x**2 * (3*r - x)) / 3

vc = vt - va


if (n == 1):
	print(round(va, 4))
	
else:
	print(round(vc, 4))
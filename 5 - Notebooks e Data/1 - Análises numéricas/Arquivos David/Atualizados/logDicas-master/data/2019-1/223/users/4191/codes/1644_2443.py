# n= 1 volume de ar, n= 2 volume de combustivel
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import pi
r=float(input("raio: "))
h=float(input("altura: "))
n=float(input("numero: "))
if (n == 1):
	V = pi*h**2 * (3*r-h)/3
else:
	V = (4*pi*r**3/3)-(pi*h**2 * (3*r - h)/ 3)
print(round(V, 4))	
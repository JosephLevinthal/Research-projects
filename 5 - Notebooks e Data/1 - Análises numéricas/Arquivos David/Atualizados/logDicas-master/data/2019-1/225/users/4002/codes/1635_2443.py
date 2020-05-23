# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
raio = float(input("raio: "))
x = float(input("altura: "))
numero = float(input("1 ou 2: "))

v1 = 4*pi*(raio**3) / 3
v2 = pi*(x**2)*(3*raio - x) / 3

if (numero == 1):
	print(round(v2, 4))
else:
	print(round(v1-v2, 4))
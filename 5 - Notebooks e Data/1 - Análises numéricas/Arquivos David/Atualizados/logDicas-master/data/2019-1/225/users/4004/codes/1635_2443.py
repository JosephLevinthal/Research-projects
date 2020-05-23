# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

r = float(input("raio: "))
h = float(input("altura: "))
n = int(input("calculo de (1/2): "))

from math import*

volume = ((4 * pi) * (r ** 3)) / 3
calota = (pi * (h ** 2) * (3 * r - h)) / 3

if (n == 1):
	msg = calota
else:
	msg = volume - calota

print(round(msg, 4))
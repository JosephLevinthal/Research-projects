# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
r = float(input(""))
x = float(input(""))
n = input("volume? (1/2)")

from math import*
if (n == "1"):
	vdc = ((pi * x ** 2 *(3 * r - x))/(3))
	print(round(vdc, 4))
else:
	vdc = ((pi * x ** 2 *(3 * r - x))/(3))
	vcomb = ((4*pi*r**3)/(3)) - vdc
	print(round(vcomb,4))
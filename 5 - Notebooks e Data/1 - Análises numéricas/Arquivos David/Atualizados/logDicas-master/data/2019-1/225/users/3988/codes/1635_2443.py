# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input("r:"))
x = float(input("altura:"))
n = float(input("numero 1 / 2:"))
if (n == 1):
	v = (pi*(x**2) * ((3*r) - x)) / 3
else:
	v = (((4 * pi * (r**3)) / 3)) - ((pi*(x**2) * ((3*r) - x)) / 3)
print(round(v , 4))	
	
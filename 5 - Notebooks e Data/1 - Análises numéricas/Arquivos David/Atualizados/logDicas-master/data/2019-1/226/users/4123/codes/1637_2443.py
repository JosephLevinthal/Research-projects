# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input())
x = float(input())
n = input()
if n == "1":
	V = pi*(x**2)*(3*r-x)/3
else:
	V = 4*pi*(r**3)/3 - pi*(x**2)*(3*r-x)/3
print(round(V, 4))

# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input("raio do tanque: "))
h = float(input("altura da coluna: "))
n = int(input("opcao: "))
if n == 1:
	v = (pi*h**2 * (3*r - h))/3
else:
	v = (4*pi*r**3)/3 - (pi*h**2 * (3*r - h))/3
print(round(v,4))
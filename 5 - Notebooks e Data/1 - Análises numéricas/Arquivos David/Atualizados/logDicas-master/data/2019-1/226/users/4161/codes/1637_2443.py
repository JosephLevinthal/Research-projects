# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input("valor do raio: "))
x = float(input("altura da coluna de ar: "))
n = int(input("volume de ar (1) / volume de combustivel (2): "))
vt = 4*pi*(r**3)/3
vc = pi*(x**2)*(3*r - x)/3
if(n == 1):
	print(round(vc, 4))
else:
	print(round(vt-vc, 4))
	
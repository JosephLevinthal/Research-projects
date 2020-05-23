# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
r = float(input(" digite r: "))
h = float(input("digite h: "))
x = int(input("digite a opcao: "))
v2 = (4*pi*(r**3))/3
v1 = (pi*(h**2)*(3*r - h))/3
v3  = v2-v1
if (x == 1):
	print(round(v1,4))
if (x == 2):
	print(round(v3,4))
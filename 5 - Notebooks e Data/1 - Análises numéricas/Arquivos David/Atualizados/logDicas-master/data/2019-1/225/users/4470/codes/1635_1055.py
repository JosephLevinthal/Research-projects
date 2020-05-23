# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
v0 = float(input())
a = radians(float(input()))
D = float(input())
g = 9.8
R = (v0)**2*sin(2*a)/g
if (abs(D-R)>0.1):
	print("nao")
else:
	print("sim")
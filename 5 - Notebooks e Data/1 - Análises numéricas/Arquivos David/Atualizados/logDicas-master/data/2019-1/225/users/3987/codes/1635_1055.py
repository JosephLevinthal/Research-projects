# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
sin
vo = float(input("inicial:"))
a = radians(float(input("angulo:")))
d = float(input("distancia:"))
R = ((vo)**2 * sin(2*a))/9.8
if abs(d>=R-0.1 and d<=R+0.1):
	print("sim")
else:
	print("nao")

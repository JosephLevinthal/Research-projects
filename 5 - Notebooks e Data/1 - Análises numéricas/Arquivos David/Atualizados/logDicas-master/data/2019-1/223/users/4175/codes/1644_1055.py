# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
v = float(input("digite a velocidade inicial em metros: "))
a = radians(float(input("digite o angulo a: ")))
d = float(input("digite a distancia horizontal em metros: "))

g = 9.8

R = ((v**2) * sin(2*a))/g

result = abs(d - R)

if  result < 0.1:
	print("sim")
else:
	print("nao")

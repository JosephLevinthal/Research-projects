# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
v0 = float(input("Digite aqui a velocidade: "))
an = radians(float(input("Digite aqui o angulo: ")))
D = float(input("Digite aqui a distancia entre o passaro e o porco: "))
g = 9.8
R = ((v0 ** 2) * (sin(2 * an))) / g
x = abs(D - R)
if (x <= 0.1):
	  msg = "sim"
else:
	  msg = "nao"
	  
print(msg)
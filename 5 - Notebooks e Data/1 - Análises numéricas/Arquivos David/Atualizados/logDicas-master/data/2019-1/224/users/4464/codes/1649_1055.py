	# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
v = float(input("insira a velocidade inicial:"))
a = radians((float(input("insira o angulo do vetor:"))))
D = float(input("insira a distancia horizontal"))
g = 9.8
R = ((v**2)*sin(2*a))/g
if (abs(D-R) <= 0.1):
	print("sim")
else:
 print("nao")
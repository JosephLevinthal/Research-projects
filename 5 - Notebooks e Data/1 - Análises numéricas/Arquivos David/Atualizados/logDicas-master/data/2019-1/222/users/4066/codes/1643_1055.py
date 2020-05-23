# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

import math

v0 = float(input("velocidade inicial: "))
a = math.radians(float(input('angulo: ')))
D = float(input('distancia: '))
g = 9.8
R = ((math.pow(v0, 2)*math.sin(2*a)))/(g)
ac = D - R
acerto = abs(ac)

if (acerto < 0.1):
	print("sim")
	
else:
	print("nao")
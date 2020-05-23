# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
vo = float (input("Digite a velocidade inicial:"))
a = float (input("Digite o angulo do vetor de lancamentos com o solo:"))
D = float (input("Digite a distancia entre o passaro e o porco:"))
g = 9.8
R = ((vo**2)*(sin(radians(2*a))))/g
if (abs(D-R)<0.1):
	print ("sim")
else:
	print("nao")

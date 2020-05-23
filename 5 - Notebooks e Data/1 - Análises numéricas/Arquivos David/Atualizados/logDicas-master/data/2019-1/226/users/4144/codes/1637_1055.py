# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
g = 9.8
vel = float(input("digite a velocidade inicial v0 (em m/s): "))
ang = float(input("digite o angulo: "))
D = float(input("digite a distancia entre o passaro e o porco: "))
ang = radians(ang)
R = ((vel)**2 * sin(2 * ang)) / g
if abs(D - R) < 0.1:
	print("sim")
else:
	print("nao")
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
vo = float(input("Velocidade inicial: "))
alpha = radians(float(input("Angulo em graus: ")))
d = float(input("Distancia entre o passaro e o porco: "))
r = (vo**2 * sin(2*alpha)) / 9.8
if abs(d - r) <= 0.1:
	print("sim")
else:
	print("nao")

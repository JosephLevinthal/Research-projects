# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
vo = float(input("Velocidade inicial:"))
an = float(input("Angulo de inclinacao:"))
dis = float(input("Distancia ate o porco:"))

r = (((vo)**2) * sin(2*radians(an))) /9.8

if (abs(dis - r) <= 0.1):
	msg = "sim"
else:
	msg = "nao"
print(msg)
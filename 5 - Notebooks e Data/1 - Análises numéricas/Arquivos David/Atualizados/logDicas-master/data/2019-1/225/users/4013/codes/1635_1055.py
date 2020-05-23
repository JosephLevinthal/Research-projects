# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
vo = float(input("velocidade inicial:"))
alpha = radians(float(input("angulo:")))
d =float(input("distancia do bird ao porco:"))

r = (((vo)**2) * sin(2*alpha))/ 9.8

if(abs(d - r) <= 0.1):
	msg = "sim"
else:
	msg = "nao"
print(msg)
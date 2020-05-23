# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v0 = float(input("Velocidade inicial em m/s: "))
a1 = float(input("Angulo em graus: "))
d = float(input("Distancia horizontal D em metros: "))
g = 9.8
a = radians(a1)

r = ((v0 ** 2) * sin(2*a)) / g
if(abs(d-r) <= 0.1):
	print("sim")
else:
	print("nao")

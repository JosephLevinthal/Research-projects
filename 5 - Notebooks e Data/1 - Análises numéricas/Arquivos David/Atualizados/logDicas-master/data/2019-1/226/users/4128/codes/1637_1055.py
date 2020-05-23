# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

vl = float(input("velocidade inicial: "))
an = radians(float(input("angulo alpha: ")))
dis = float(input("distancia percorrida: "))
r = (vl**2) * sin(2*an)/ 9.8
if(abs(r - dis) <= 0.1):
	print("sim")
else:
	print("nao")
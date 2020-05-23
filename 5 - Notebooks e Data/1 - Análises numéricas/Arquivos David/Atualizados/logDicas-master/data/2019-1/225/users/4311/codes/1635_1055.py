# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
vi = float(input("Velocidade inicial: "))
an = radians(float(input("angulo: ")))
d = float(input("distancia horizontal: "))
g = 9.8
R = ((vi**2)*sin(2*an))/g
if(abs(R-d)<= 0.1):
	print("sim")
else:
	print("nao")
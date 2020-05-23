# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
vo = float(input("velocidade inicial: "))
a = radians(float(input("angulo do vetor: ")))
d = abs(float(input("distancia: ")))
g = 9.8

r = ((vo)**2) * sin(2*a)
r1 = r/g

if(abs(r1 - d) <= 0.1):
	print("sim")
					  
else:
	print("nao")

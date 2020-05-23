# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

from math import*

v = float(input("Qual a velocidade? "))
alfa = radians(float(input("Qual o angulo? ")))
D = float(input("Qual a distancia? "))

g = 9.8

d = ((v**2) * sin(2*alfa)) / g

if(abs(D - d <=  0.1)):
	print("sim")
else:
	print("nao")
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v0 = float(input("velocidade inicial: "))
angulo = float(input("angulo do vetor: "))
distancia = float(input("distancia: "))
g = 9.8

a = radians(angulo)

r = ((v0**2)*sin(2*a))/9.8

r1 = abs(distancia - r)

if  ( r1 <= 0.1):
     print("sim")
		
else:
	 print("nao")
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
velocidade_inicial = float(input("velocidade inicial: "))
angulo = radians(float(input("angulo: ")))
distancia = float(input("valor das entradas: "))

R = ((velocidade_inicial**2) * sin(2*angulo)) / 9.8

p = distancia - R

if(abs(p < 0.1)):
	print("sim")
else:
	print("nao")



# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
velocidade_inicial = float(input("velocidade inicial: "))
angulo = radians(float(input("angulo de lancamento: ")))
distancia_porco = float(input("digite a distancia entre o passaro e o porco: "))
gravidade = 9.8
distancia = ((velocidade_inicial ** 2) * sin(2 * angulo)) / gravidade

if (distancia == distancia_porco) :
	print("sim")
if (abs(distancia_porco - distancia) <= 0.1) : 
	print("sim")
else :
	print("nao")
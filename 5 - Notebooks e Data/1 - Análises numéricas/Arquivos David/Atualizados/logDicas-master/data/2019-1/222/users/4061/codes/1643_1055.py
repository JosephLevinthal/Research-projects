# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

velocidade = float(input("digite velocidade inicial: "))
angulo = float(input("digite angulo: "))
distancia = float(input("digite a distancia: "))
gravidade = 9.8
r = ((radians(2*angulo)))/gravidade
absoluto = distancia - abs(r - distancia)
if (absoluto > 0.1):
	mensagem = ("sim")
else: 
	mensagem = ("nao")
print(mensagem)

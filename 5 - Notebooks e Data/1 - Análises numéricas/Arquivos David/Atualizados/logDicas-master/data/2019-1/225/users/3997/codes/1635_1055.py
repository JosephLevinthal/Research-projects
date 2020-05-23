# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
Vo = float(input("digite Vo:"))
alpha = radians(float(input("Digite o alpha: ")))
D = float(input("Digite uma distancia: "))

g = 9.8
R = (Vo ** 2 * sin (2 * alpha)) / g

if (abs(D - R) < 0.1):
	print("sim")
else: 
	print("nao")


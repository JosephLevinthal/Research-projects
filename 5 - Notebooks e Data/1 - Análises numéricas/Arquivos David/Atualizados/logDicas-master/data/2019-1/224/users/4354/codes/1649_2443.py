# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
raio = float(input("digite o raio: "))
altura_coluna = float(input("digite a altura da coluna de ar: "))
opcao_de_calculo = float(input("digite a opcao de calculo 1 ou 2: "))
volume_da_calota = (pi * ((altura_coluna) ** 2) * (3 * raio - altura_coluna)) / 3 
volume_da_esfera = (4 * pi * raio ** 3) / 3
volume_combustivel = volume_da_esfera - volume_da_calota
if(opcao_de_calculo == 1) :
	print(round(volume_da_calota,4))
if(opcao_de_calculo == 2) :
	print(round(volume_combustivel,4))

	
							 
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
import math


V0 = float(input())

a = float(input())

distancia = float(input())

g = 9.8

angulo = math.radians(a)

r = ((V0**2) * math.sin(2*angulo))/g

absoluto = abs(distancia - r)


if( absoluto > 0.1):
	print('nao')

elif (absoluto < 0.1):
	print('sim')
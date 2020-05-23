# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

v1 = float(input('inicial: '))
ang = radians(float(input('angulo: ')))
D = float(input('distancia: '))
g = 9.8
R = ((((v1)**2 ) * sin(2* ang))/(g))
if(abs(D - R) <= 0.1):
	print('sim')
else:
	print('nao')
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v=float(input('velocidade inicial:'))
a=radians(float(input('angulo de tiro:')))
d=float(input('valor da distancia:'))
r=((v**2)*sin(2*a))/9.8
p=d-r
if(abs(p)<0.1):
	print('sim')
else:
	print('nao')
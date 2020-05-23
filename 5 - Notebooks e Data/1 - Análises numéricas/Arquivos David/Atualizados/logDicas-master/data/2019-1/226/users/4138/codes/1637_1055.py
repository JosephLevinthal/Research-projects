# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
vo = float(input("insira velocidade inicial: "))
a = float(input("insira o angulo: "))
D = float(input("insira a distancia: "))
g = 9.8

A = radians(2 * a)
R = ((vo ** 2) * sin(A))/g
	
r = abs(D - R)
if (r < 0.1):
	mensagem = "sim"
else:
	mensagem = "nao"
	
print(mensagem)

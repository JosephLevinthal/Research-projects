# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

v = float(input("Velocidade: "))
a = float(input("Angulo: "))
D = float(input("Distancia: ")) 

a = radians(a)

R = ((v**2) * sin(2*a)) / 9.8

if ( abs(D - R) < 0.1):
	mensagem = "sim"
else:
	mensagem = "nao"
	
print(mensagem)
	
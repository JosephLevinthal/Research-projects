# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
vo = float(input("velocidade inicial: "))
a = radians(float(input("ang: ")))
dis = float(input("distancia: "))
g = 9.8
#formula
R = ((vo ** 2) * (sin*2*a) / g )
if((abs(dis - R) <= 0.1) and (abs(dis - R) >= 0)):
	mensagem = "sim"
else:
	mensagem = "nao"
	
print(mensagem)

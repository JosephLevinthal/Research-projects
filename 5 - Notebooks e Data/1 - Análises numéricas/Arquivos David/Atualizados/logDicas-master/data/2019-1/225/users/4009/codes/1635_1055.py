# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v0 = float(input("velocidade inicial: "))
a = radians(float(input("angulo: "))
d = float(input("distancia: "))
g = 9,8
r=(v0**2)*sin(2a)
R = r/g
				
if abs(d-R) <= 0.1:
	mensagem = "sim"
	print(mensagem)
else:
	mensagem = "nao"
	print(mensagem)		
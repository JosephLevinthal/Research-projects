# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v = float(input("Velocidade inicial: "))
a = radians(float(input("Angulo: ")))
g = 9.8
D = float(input("Distancia horizontal: "))
R = ((v**2) * sin(2*a))/g
if (abs(R-D) <= 0.1):
	mensagem = "sim"
	print(mensagem)
else:
	mensagem = "nao"
	print(mensagem)
	
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
Vi = float(input("Digite a velocidade inicial: "))
ang = float(input("Digite o angulo: "))
d = float(input("Digite a distancia em metros: "))
from math import *
g = 9.8
rad = radians(ang)
r = (Vi)**2 * sin(2 * rad) / g
if(abs(d - r) < 0.1):
	mensagem = "sim"
	print(mensagem)
else:
	mensagem = "nao"
	print(mensagem)
	


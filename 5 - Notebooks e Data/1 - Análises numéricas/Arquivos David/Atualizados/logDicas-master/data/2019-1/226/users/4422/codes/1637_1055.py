# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
vo = float(input("velocidade: "))
a = radians(float(input("angulo: ")))
d = abs(float(input("distancia: ")))
g = 9.8
r = ((vo)**2 * sin(2 * a))/g
if(r >= d - 0.1):
	mensagem = "sim"

else:
	mensagem = "nao"
	
print(mensagem)


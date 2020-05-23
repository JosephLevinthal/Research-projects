# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
v0 = float(input("escreva o valor da velicidade inicial: "))
a = radians(float(input("escreva o valor do angulo: ")))
d = float(input("escreva a distancia entre o passaro e o porco: "))
r = ((v0**2)*sin(2*a))/9.8
p = d - r
if (abs(p) < 0.1):
	mensagem = "sim"
else:
	mensagem = "nao"
				
print(mensagem)
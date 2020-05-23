# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
v = float(input("Digite a velocidade inicial (m/s): "))
a = float(input("Digite o angulo de lancamento (em graus): "))
d = float(input("Distancia horizontal: "))
g = 9.8
from math import *
A = radians(a)
b = sin(2*A)
dist =((v**2) * b)/g
x = abs (dist - d)

if (x < 0.1):
	resp= "sim" 
	print(resp)
else:
	resp= "nao"
	print(resp)
	
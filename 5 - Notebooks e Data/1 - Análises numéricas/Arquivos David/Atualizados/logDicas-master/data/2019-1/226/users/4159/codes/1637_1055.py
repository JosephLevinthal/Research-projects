# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
vo = float(input("velocidade inicial: "))
a = radians(float(input("angulo: ")))
g = 9.8
d = float(input("porco: "))
r = (vo**2*sin(2*a))/g
if(abs(d-r) <= 0.1):
	print("sim")
else:
	print("nao")
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v=float(input("velocidade inicial: "))
a=radians(float(input("angulo do tiro: ")))
d=float(input("valor da distancia: "))
g=9.8
r=((v**2)*sin(2*a))/g
p=d-r
if(abs(p)<0.1):
	print("sim")
else:
	print("nao")
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
v=float(input("velocidade inicial: "))
a=(float(input("angulo de lancamento: ")))
D=float(input("distancia inicial: "))
g=9.8
from math import *
R= (v**2)*sin(2*radians(a))/g
d=abs(D-R)
if R+0.1>D:
	print("sim")
else:
	print("nao")
	
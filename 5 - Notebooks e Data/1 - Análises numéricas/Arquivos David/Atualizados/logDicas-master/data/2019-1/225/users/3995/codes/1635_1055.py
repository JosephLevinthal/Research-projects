# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
V0=float(input("velocidade inicial:"))
from math import*
a=radians(float(input("angulo de lancamento:")))
D=float(input("distancia:"))
R=((V0**2)*(sin(2*a)))/9.8
h=abs(D-R)
if(h<=0.1):
	print("sim")
else:
	print("nao")
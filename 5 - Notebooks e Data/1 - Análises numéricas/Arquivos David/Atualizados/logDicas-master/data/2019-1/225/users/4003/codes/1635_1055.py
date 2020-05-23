# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

vi=float(input("velocidade inicial:"))
angulo=radians(float(input("angulo(em graus):")))
D=float(input("Distancia:"))
g=9.8

r=(vi**2)*sin(2*angulo)/g

if(abs(D-r)<=0.1):
	print("sim")

else:
	print("nao")
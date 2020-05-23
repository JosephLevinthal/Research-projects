# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v0=float(input("Digite a velocidade inicial:"))
a=radians((float(input("Digite o angulo do vetor:"))))
d=float(input("Digite a distancia horizontal:"))
g=9.8
r=((v0**2)*sin(2*a))/g
if(abs(d-r)<=0.1):
	print("sim")
else:
	print("nao")
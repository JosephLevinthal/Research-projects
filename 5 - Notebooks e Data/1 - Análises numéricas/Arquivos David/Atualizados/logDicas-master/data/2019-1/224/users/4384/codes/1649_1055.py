# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v=float(input("v inicial:   "))
a=float(input("angulo:   "))
d=float(input("distancia:   "))
r=((v**2)*(sin(2*(radians(a)))))/9.8
r=abs(r)
if(d-r)<0.1:
	print("sim")
else:
	print("nao")
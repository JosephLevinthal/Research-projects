# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
a=float(input("v0:"))
b=float(input("valor do angulo:"))
c=float(input("distancia do passaro ao porco:"))
b2=(radians(b))
eq=(((a)**2)*sin(2*b2))/9.8
d=abs(eq-c)
if(d<0.1):
	print("sim")
else:
	print("nao")
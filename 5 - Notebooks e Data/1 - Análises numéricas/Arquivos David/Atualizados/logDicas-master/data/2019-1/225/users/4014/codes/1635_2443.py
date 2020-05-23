# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
r=float(input("raio:"))
x=float(input("altura:"))
w=int(input("1 ou 2?"))
from math import*
V=(4*pi*(r**3))/3
V2=(pi*(x**2)*(3*r-x))/3
if(w ==1):
	print(round(V2,4))
else:
	print(round(V-V2,4))
	
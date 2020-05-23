# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
r=float(input("raio: "))
x=float(input("altura: "))
z=input("opcao 1 ou 2: ")
from math import *
opcao1=(pi*(x**2)*(3*r-x))/3
opcao2=((4*pi)*(r**3))/3
if(z=="1"):
	print(round(opcao1,4))
else:
	print(round(opcao2-opcao1,4))

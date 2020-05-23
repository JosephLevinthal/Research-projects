# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
r=float(input("raio: "))
x=float(input("Altura da coluna de ar: "))
op=input("Qual a opcao desejada: 1/2 ")
V=pi*x**2*(3*r-x)/3
v=4*pi*r**3/3
if (op == "1"):
	print(round(V,4))
else:
	print(round(v-V,4))
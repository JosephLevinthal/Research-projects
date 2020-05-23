# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r=float(input("raio:"))
x=float(input("altura da coluna de ar:"))
num=input("1 ou 2?")
V=4/3*pi*r**2*r
Var=pi*x*x*(3*r-x)*1/3
if(num=="1"):
	print(round(Var,4))
else:
	print(round(V-Var,4))
	
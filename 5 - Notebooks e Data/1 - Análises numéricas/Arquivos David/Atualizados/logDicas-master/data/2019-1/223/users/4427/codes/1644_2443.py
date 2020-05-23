# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r=float(input("raio do tanque:"))
x=float(input("altura da coluna de ar na parte superior do tanque:"))
N=input("opcao desejada:")

v=pi*x**2*(3*r-x)/3
r=4*pi*r**3/3
s=r-v

if(N=="1"):
	p=v
else:
	p=s

print(round(p,4))
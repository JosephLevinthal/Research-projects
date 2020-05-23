# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
r=float(input("raio: "))
h=float(input("altura x: "))
n=int(input("1 para volume do ar e 2 volume de cobustivel: "))
from math import *
Ve=(4*pi*(r)**3)/3
Vc=(pi*(h**2)*(3*r-h))/3
if(n==1): 
	Va=abs(Vc)
	print(round(Va,4))
if(n==2):
	Vc=abs(Ve-Vc)
	print(round(Vc,4))

	
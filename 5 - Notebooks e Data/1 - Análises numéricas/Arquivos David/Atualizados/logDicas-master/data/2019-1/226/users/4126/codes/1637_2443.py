# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r= float(input("raio:"))
x= float(input("altura:"))
opcao= int(input("numero 1 ou 2:"))
esfera= (4* pi *r**3)/3
calota= (pi * x**2 *(3*r-x))/3
comb= esfera-calota
ar=calota
if(opcao==1):
	print(round(ar,4))
else:
	print(round(comb,4))

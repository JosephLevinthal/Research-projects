# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
pi
r = float(input("raio:"))
h= float(input("altura:"))
n=int (input("opcao"))
v1=(4* pi * r**3)/3
v2=(pi * h**2 * (3*r-h))/3
if ( n== 1):
	print(round(v2,4))
else:
	h=v1-v2
	print(round(h,4))
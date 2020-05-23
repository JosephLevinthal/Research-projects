# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input("raio:"))
a = float(input("altura:"))
n = int(input("numero: (1/2)"))
v1 =(pi*(a**2)*(3*r-a))/3 
v2 = ((4*pi*(r**3))/3) - v1
if(n == 1):
	print(round(v1, 4))
else:
	print(round(v2, 4))
	

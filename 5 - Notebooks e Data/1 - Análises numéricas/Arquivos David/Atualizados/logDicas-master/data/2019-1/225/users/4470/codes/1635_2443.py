# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
r = float(input())
x = float(input())
num = int(input())#1 ou 2
V = (4*pi*r**3)/3
Ve = (pi*x**2)*(3*r-x)/3 

if (num == 1):
	print(round(Ve, 4))
	
else:
	print(round(V-Ve, 4))
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

r = float(input("raio: "))
x= float(input("altura: "))
n = int(input("volume 1/2?"))

v = (4/3)*pi*(r**3)
v2= (pi*(x** 2)*(3*r-x))/3#ar

if (n==1):
	print(round(v2,4))
else:
	x=v-v2
	print(round(x,4))
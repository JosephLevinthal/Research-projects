# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v = float(input("velo:"))
a= radians(float(input("ang:")))
d= abs(float(input("dist:")))
g= 9.8
r= ((v)**2 * sin(2*a))/g
if (r >= d -0.1):
	print("sim")
else:
	print("nao")
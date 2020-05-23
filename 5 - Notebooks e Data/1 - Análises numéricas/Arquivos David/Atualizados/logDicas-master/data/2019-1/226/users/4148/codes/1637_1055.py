# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
g = 9.8
v0 = float(input("v0: "))
a = float(input("angulo: "))
d = float(input("distancia: "))
r = (v0) **2 * sin(2*(radians(a)))/g
F = abs(r-d)
if F < 0.1:
			print("sim")	
	
else:
	print("nao")
	



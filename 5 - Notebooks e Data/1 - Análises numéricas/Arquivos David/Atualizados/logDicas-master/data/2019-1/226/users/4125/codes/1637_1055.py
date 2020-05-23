# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
vo = float(input("digite a vo: "))
a1= (float(input("digite a: ")))
d = float(input("digite a dH: "))
g = 9.8
a = radians(a1)
r = ((vo**2) * (sin(2*a))/g)
if (abs(d-r)<=0.1):
	print("sim")
else:
	print("nao")
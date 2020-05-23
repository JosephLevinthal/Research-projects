# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v0 = float(input("v0: "))
a = radians(float(input("a: ")))
d = float(input("d: "))

r = (v0**2)*sin(2*a) / 9.8

if abs(d-r) <= 0.1:
	print("sim")
else:
	print("nao")
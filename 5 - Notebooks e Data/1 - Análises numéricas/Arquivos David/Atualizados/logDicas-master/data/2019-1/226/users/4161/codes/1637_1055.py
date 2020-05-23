# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v = float(input("velocidade inicial: "))
x = radians(float(input("angulo em graus: ")))
d = float(input("distancia horizantal: "))
r = (v**2) * sin(2*x) /9.8
if (abs(r - d) <= 0.1): 
	print("sim")
else:
	print("nao")
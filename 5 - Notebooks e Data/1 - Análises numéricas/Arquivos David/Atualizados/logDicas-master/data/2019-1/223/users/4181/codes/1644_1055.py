# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import * 
vo = float(input("Valocidade inicial: "))
a = radians(float(input("Angulo: ")))
D = abs(float(input("Distancia: ")))
g = 9.8
R = ((vo)**2*sin(2*a)/g)
if (D - R < 0.1):
	print("sim")
else: 
	print("nao")
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

vo = float(input("velcidade inicial: "))
a =radians(float(input("angulo do vetor em graus: ")))
d = float(input("distancia em d: "))

r = ((vo**2) * sin(2*a))/9.8
if abs(d>=r-0.1 and d<=r+0.1):
	print("sim")
else: 
	print ("nao")
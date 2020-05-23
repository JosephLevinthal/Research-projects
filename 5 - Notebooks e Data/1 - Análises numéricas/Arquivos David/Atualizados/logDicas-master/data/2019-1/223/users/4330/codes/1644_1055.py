# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v0 = float(input("velocidade inicial: "))
a = radians(float(input("angulo do vetor: ")))
D = float(input("disntacia entre o passaro e o porco: "))
g = 9.8

R = ((v0**2)*(sin(2*a))) / g

tolerancia = abs ( D - R )

if ( tolerancia <= 0.1 ):
	print("sim".lower())
	
else:
	print("nao".lower())

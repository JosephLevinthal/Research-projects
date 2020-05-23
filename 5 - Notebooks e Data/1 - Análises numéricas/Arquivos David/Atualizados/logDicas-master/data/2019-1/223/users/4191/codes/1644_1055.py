# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import radians
from math import sin
vl=float(input("Velocidade inicial: "))
a=radians(float(input("angulo do vetor: ")))
D=float(input("Distancia horizontal: "))
g=9.8
R = vl**2 * sin(2*a) / g
if (abs(D - R <= 0.1)):
	m= "sim"
else:
	m= "nao"
print(m)	



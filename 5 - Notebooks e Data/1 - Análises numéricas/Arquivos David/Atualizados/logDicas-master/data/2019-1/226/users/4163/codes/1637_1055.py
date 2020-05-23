# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

a = float(input("velocidade inicial: "))
b = radians(float(input("angulo de alfa: ")))
d = abs(float(input("distancia horizontal D: ")))
g = 9.8
r = ((a)**2)*(sin(2*b))/g
if abs(d-r) < 0.1:
	msg = "sim"
else:
	msg = "nao"
	
print(msg)	
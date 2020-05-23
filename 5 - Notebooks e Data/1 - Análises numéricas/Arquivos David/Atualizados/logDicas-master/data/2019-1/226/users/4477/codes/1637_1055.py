# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
vo = float(input("Determine a velocidade inicial: "))
a = float(input("Determine o angulo: "))
D = float(input("Determine a distancia horizontal: "))
g = 9.8

A = radians(a)
S = sin(2*A)
R = ((vo**25)*S)/g

tol = abs (D - R)

if (tol < 0.1):
	msg = "sim"
else:
	msg = "nao"
	
print (msg)
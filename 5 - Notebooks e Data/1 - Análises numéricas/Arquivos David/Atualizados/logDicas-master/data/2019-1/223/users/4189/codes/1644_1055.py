# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

V= float(input("velocidade inicial: "))

ANG= radians(float(input("angulo: ")))

D=float(input("distancia: "))

g = 9.8

R= (V) ** 2 * sin( 2  * ANG )  / g

t= abs(D-R)


if (t<0.1):
	men="sim"
else:
	men="nao"
	
print(men)
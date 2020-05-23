from math import *
n = int(input())
calculo = 0
v = 0
a = 0
sinal = 1
while(v<n):
	denominador = ((2*v)+1)*(3**a)
	x = 12**(1/2) * (sinal*1)/denominador
	calculo = calculo + x
	v = v+ 1
	sinal = sinal * (-1)
	a = a + 1
print(round(calculo,8))
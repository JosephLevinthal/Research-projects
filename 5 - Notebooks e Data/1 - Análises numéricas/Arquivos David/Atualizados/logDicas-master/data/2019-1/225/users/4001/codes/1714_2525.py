from math import *
n = int(input("Numero: "))
a = 0 #variavel acumuladora(qtd. de divisores)
cont = 0 #variavel contadora
v = 1
while (n % v == 0):
	print(v)
	v = v + 1
	a = a + 1
	if (n % v != 0):
		v = v + 1	
if (v == n):
	print(a, "divisores")
if (n == 1):
	print(1, "divisor")

		
	
	
	
		
	
	

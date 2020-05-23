from math import *

n = int(input("insira o number de termos: "))

ap = 0
cont = 1

while (cont <= n):
	ap = ap + 6/cont**2
	cont += 1

print(round(sqrt(ap),6))
from math import *
n = int(input("Digite n :"))
cont = 1
sinal = 1
pii = 3
c = 2

if n == 1:
	print(pii)
else:
	while cont < n:
		termo =  4 / ((c)*(c + 1)*(c + 2))
		c = c + 2
		pii = pii + (termo * sinal)
		cont = cont + 1
		sinal = sinal * (-1)
print(round(pii,8))
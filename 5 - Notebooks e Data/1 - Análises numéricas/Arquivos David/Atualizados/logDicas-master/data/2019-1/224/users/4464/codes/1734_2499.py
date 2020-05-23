from math import *

k = int(input("Digite o numero natural: "))
e = 0.0
cont = 0

while (cont < k):
	e = e + (1.0/factorial(cont))
	cont = cont + 1
print(round(e,8))
# Instituto de Computacao - UFAM
# Nathaly Leite

from math import *

k = int(input("Informe um numero: "))

i = 0
e = 0

while (i < k):
	e = e + (1 / factorial(i))
	i = i + 1
	
print (round(e,8))
	
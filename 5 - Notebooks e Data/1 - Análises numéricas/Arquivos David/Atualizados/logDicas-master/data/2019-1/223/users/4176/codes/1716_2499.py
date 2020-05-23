k= int(input("Numero Real k: "))

cont= 0
var= 0

from math import*

while (cont < k):
	var= var + (1/factorial(cont))
	cont= cont + 1
print(round(var,8))
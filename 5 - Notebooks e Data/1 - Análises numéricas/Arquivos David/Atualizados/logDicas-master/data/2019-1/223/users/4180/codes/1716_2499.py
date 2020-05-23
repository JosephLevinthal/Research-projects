from math import*

cont = 0
var = 0 

k = int(input("N Real K: "))

while(cont < k):
	var = var +(1/factorial(cont))
	cont = cont + 1
print(round(var , 8))
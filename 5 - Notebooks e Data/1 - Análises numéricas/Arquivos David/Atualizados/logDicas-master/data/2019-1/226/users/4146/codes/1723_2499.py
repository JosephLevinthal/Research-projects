from math import*

k = int(input("Quantas casas: "))
x = 0
e = 0
while (x <= k - 1):
	e = 1/factorial(x) + e
	x = x + 1
	
print(round(e, 8))	
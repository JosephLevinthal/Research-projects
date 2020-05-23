k = int(input("Digite K: "))

from math import*
e = 1
r = 1
x= 0
while (k > r):
	x = 1/factorial(r)
	r = r + 1
	e = e + x
	
print(round(e, 8))
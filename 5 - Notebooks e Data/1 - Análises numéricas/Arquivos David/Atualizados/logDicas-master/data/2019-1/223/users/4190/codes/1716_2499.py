from math import *
k = int(input('Numero natural: '))

c = 1
r = 1
e = 1

while (c<k):
	r = r+(1/factorial(e))
	e+= 1
	c+=1
print(round(r, 8))
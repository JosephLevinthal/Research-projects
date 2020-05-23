from math import*

k=int(input("Numero natural: "))

c=0
e=0

while(c<k):
	e=e+(1/factorial(c))
	c=c+1
print(round(e,8))
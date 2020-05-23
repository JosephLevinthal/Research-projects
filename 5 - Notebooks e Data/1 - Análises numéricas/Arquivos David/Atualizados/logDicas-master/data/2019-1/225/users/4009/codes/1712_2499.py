from math import*

g= float(input())

e= 0
c= 0

while (c<g):
	e= e + (1/factorial(c))
	c= c + 1
print(round(e,8))


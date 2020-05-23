from math import*
c= int(input())

g = 0
e = 0

while(g<c):
	e = e +(1/factorial(g))
	g = g+1
	
print(round(e,8))
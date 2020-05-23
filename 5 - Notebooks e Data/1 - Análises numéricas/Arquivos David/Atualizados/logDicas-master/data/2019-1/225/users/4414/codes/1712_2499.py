from math import*

k= int(input("k:"))

c=0
e=0

while(k>c):
	e=e+ (1/factorial(c))
	c=c+1
	
print(round(e,8))
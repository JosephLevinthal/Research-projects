from math import *
x = eval(input("x: "))
k = int(input("k: "))

h = 1
s = -1
x1 = x
e = 3
while k>h:
	x1 = x1 + s*((x**e)/factorial(e))
	e += 2
	h += 1 
	s = s *-1
	

print(round(x1,10))
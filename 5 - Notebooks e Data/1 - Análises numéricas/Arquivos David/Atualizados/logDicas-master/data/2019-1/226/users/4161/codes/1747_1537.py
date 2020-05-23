from math import*
x = float(input("valor de x: "))
k = int(input("serie: "))
t = 1
s = 1
if k == 1:
	s == 1.0
else:	
	while t<=(k-1):
		s = s + (x**t)/factorial(t)
		t = t + 1
print(round(s, 9))
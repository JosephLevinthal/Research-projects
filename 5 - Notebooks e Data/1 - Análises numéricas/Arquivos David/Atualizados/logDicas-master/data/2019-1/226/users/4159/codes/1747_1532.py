from math import*
x = float(input("x "))
k = int(input("k "))
som = x
l = 1
v = 3
while(k>l):
	som = som + (x**v)/factorial(v)
	v = v+2
	l = l+1
print(round(som, 9))
	
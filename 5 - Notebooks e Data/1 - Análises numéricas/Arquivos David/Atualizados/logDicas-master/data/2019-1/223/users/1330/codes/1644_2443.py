from math import *
r = float(input())
a = float(input())
n = int(input())

if n == 1:
	v =(((pi*(a**2)) * (3*r - a))/3)
	print(round(v, 4))
else:
	v = ((4*pi*(r**3)) / 3) - (((pi*(a**2)) * (3*r - a))/3) 
	print(round(v,4))
from math import*

v = float(input())
a = float(input())
d = float(input())

g = 9.8
x = radians(a)
r = ( ( (v)**2) * ( sin(2*x) ) )/g
y=abs(d-r)
if( y<= 0.1):
	print("sim")
else:
	print("nao")
from math import *

vi = float(input())
a = radians(float(input()))
d = float(input())
g=9.8

r = ((vi**2)*sin(2*a))/g

if(abs(d-r)<0.1 ):
	print("sim")
else:
	print("nao")
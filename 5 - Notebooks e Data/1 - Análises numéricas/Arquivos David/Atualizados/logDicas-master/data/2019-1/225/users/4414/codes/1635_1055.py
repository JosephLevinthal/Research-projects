from math import sin
from math import radians 

vo=float(input("veloci:"))
a=radians(float(input()))
g=9.8
d=float(input())

r=(vo**2)*sin(2*a) /g
if abs(d-r)>0.1:
	print("nao")
else:
	print("sim")
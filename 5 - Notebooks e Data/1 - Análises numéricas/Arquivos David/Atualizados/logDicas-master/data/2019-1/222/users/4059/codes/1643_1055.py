import math

v0=float(input())
a=math.radians(float(input()))
d=float(input())
g=9.8
R=((v0**2)*math.sin(2*a))/g
if ((abs(d-R))<0.1):
	print("sim")
else:
	print("nao")
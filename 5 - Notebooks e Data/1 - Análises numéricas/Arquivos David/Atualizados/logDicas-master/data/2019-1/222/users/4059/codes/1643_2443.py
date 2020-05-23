import math
r=float(input())
x=float(input())
ops=int(input())
VE=(4*math.pi*r**3)/3
VC=(math.pi*(x**2)*((3*r)-x))/3
if (ops==2):
	print(round(VE-VC,4))
if (ops==1):
	print(round(VC,4))
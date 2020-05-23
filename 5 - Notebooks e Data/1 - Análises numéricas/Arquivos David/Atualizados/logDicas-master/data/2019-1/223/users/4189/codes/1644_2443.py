r = float(input("raio:"))
x = float(input("altura:"))
n = int(input("1,2:"))
from math import *
VC = (pi*(x**2)*((3*r)-x))/(3)
VE = (4*pi*r**3)/3
if(n==1):
	print(round(VC,4))
else:
	print(round(VE-VC,4))
	
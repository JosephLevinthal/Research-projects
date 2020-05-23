from math import *

r = float(input())
a = float(input())
op = int(input())

if(op==1):
	v = ( ( pi*a**2) * (3 * r - a) )/3
	print(round(v,4))
if(op==2):
	v1 = (4*pi*r**3)/3
	v2 = ( ( pi*a**2) * (3 * r -a) )/3
	print(round((v1-v2),4))

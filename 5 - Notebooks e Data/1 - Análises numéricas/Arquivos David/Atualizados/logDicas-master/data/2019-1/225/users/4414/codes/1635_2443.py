from math import pi
r = float(input("raio:"))
x = float(input("altura:"))
a = float(input("1 ou 2"))

v1= (4*pi*r**3)/3
v2= (pi*x**2)*(3*r-x)/3
if (a==1):
	print(round(v2,4))
else: 
	print(round(v1-v2,4))
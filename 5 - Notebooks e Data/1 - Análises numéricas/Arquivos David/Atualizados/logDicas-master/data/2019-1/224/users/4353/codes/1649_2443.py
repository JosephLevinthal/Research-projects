from math import*
r=float(input("raio: "))
x=float(input("altura: "))
c=input("1 ou 2: ")
v2=(pi*(x**2))*((3*r)-x)/3
v1=((4*pi)*(r**3))/3
if(c=="1"):
	print(round(v2,4))
else:
	print(round(v1-v2,4))


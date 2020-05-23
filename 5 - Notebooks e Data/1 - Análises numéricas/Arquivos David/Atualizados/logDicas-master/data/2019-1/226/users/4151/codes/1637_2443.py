from math import*
r=float(input("raio do tanque: "))
a=float(input("altura: "))
x=int(input("opcao: "))
v1=(4*pi*r**3)/3
v2= (pi * (a)**2 * (3*r-a))/3

if(x== 1):
	print(round(v2,4))
else:
	print(round(v1-v2,4))

from math import*
v=float(input("velocin:"))
a=radians(float(input("angti:")))
d=float(input("dist:"))
r=((v**2)*sin(2*a))/9.8
p=d-r
if(abs(p) < 0.1):
	print("sim")
else:
	print("nao")
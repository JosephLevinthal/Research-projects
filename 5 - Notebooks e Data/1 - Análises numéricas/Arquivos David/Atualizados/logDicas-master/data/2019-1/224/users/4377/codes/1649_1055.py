v0=float(input("v0"))
angu=float(input("angu"))
D=float(input("D"))
from math import*
R=((v0**2)*sin(radians(2*angu))) / 9.8

if (abs(D-R)<0.1):
	print("sim")
else:
	print("nao")
from math import*
r=float(input(""))
X=float(input(""))
n=float(input("1/2:"))

V=  4*pi*r**3/ 3
Ve= pi* X**2* (3*r-X)/3
Vc= V-Ve
if (n == 1):
	print(round(Ve,4))
else:
	print(round(Vc,4))
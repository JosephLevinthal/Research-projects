from math import*
r = float(input())
x = float(input())
num = int(input())
V = (4*pi*r**3)/3
Ve =(pi*x**2)*(3*r-x)/3
if (num == 1):
	print(round(Ve, 4))
else:
	print(round(V-Ve, 4))
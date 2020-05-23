from math import *
x = float(input("Digite x : "))

if ((x >= 0 and x <90) or (x>= 180 and x< 270 )):
	a = sin(radians(x))
	print(round(a,4))
elif ((x>= 90 and x<180) or (x <= 270 and x <360)):
	a = cos(radians(x))
	print(round(a,4))
elif (x<0 or x> 360):
	print("entrada invalida")
from math import *

x = float(input("x: "))

if x >= -1 <= x < (-1/2) or (1/2) < x <= 1:
	fx = degrees(asin(x))
	print(round(fx,2))
elif (-1/2) <= x <= (1/2):
	fx = degrees(acos(x))
	print(round(fx,2))
else:
	print("entrada invalida")



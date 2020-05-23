from math import*
x = float(input("x: "))

if (0 <= x) and (x < 90) or (180 <= x) and (x < 270):
	f = radians(x)
	F = sin(f)
	print(round(F, 4))
elif (90 <= x) and (x < 180) or (270 <= x) and (x < 360):
	f = radians(x)
	F = cos(f)
	print(round(F, 4)) 
else:
	print("entrada invalida")
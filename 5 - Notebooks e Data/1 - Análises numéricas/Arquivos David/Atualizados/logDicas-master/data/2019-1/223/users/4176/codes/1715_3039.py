from math import*

x= float(input("Valor para x: "))

if (((-1) <= x < (-0.5) or (0.5 < x <= 1))):
	print(asin(degrees(round(x),2)))
else:
	print("entrada invalida")
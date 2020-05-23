from math import*
x = radians(input("Valor de x: "))

if(0 <= x) and (x < 90) or (x == 180):
	print(round(sin(x), 4)
elif(90 <= x) and (x < 180) or (x == 270):
	print(round(cos(x), 4)
else:
	print("entrada invalida")
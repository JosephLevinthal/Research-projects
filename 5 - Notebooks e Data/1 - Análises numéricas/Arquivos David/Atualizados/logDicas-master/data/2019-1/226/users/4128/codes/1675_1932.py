from math import*

do1 = float(input("distancia entre os olhos 1: "))
dnq1 = float(input("distancia entre o nariz e o queixo 1: "))
do2 = float(input("distancia entre os olhos 2: "))
dnq2 = float(input("distancia entre o nariz e o queixo 2: "))
do3 = float(input("distancia entre os olhos 3: "))
dnq3 = float(input("distancia entre o nariz e o queixo 3: "))

f1 = do1/dnq1
f2 = do2/dnq2
f3 = do3/dnq3

x = abs(f1 - f2)
y = abs(f2 - f3)
z = abs(f1 - f3)

if((x < y) and (y > z)):
	print("1 e 3")
elif((x < y) and (z > y)):
	print("1 e 2")
elif((x < z) and (z > y)):
	print("1 e 2")
elif((x < z) and (y > z)):	
	print("1 e 3")

elif((y < x) and (x > z)):
	print("2 e 1")
elif((y < x) and (z > x)):
	print("2 e 3")
elif((y < z) and (z > x)):
	print("2 e 3")
elif((y < z) and (x > z)):
	print("2 e 1")

elif((z < x )and (x > y)):
	print("3 e 1")
elif((z < x) and (y > z)):
	print("3 e 2")
elif((z < y) and (y > x)):
	print("3 e 2")
else:
	print("3 e 1")
#Lendo as variaveis

a = float(input("Distancia entre os olhos: "))
a1 = float(input("Distancia entre o nariz e o queixo: "))
b = float(input("Distancia entre os olhos: "))
b1 = float(input("Distancia entre o nariz e o queixo: "))
c = float(input("Distancia entre os olhos: "))
c1 = float(input("Distancia entre o nariz e o queixo: "))

# Razao P
p1 = abs(a / a1)
p2 = abs(b / b1)
p3 = abs(c / c1)

if (abs(p1 - p2) > abs(p1 - p3)) and (p1 > p2):
	print (1, "e ",2)
elif (abs(p1 - p2) > abs(p1 - p3)) and (p1 < p2):
	print(2, "e ",1)
elif (abs(p1 - p3) > abs(p1 - p2)) and (p1 > p3):
	print(1, "e ",3)
elif (abs(p1 - p3) > abs(p1 - p2)) and (p1 < p3):
	print(3, "e ",1)
elif (abs(p2 - p3) > abs(p2 - p1)) and (p2 > p3):
	print(2, "e ",3)
elif (abs(p2 - p3) > abs(p2 - p1)) and (p2 < p3):
	print(3, "e ",2)
elif (p1 == p2) and (p1 != p3):
	print (1, "e ",2)
elif (p1 == p3) and (p1 != p2):
	print(1, "e ",3)
elif (p2 == p3) and (p1 != p2):
	print(2, "e ",3)
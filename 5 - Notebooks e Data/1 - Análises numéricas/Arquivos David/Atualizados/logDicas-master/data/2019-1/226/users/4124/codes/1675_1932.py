from math import *
o1 = float(input("Distancia entre os olhos 1: "))
n1 = float(input("Distancia entre o nariz e queixo 1: "))
o2 = float(input("Distancia entre os olhos 2: "))
n2 = float(input("Distancia entre o nariz e queixo 2: "))
o3 = float(input("Distancia entre os olhos 3: "))
n3 = float(input("Distancia entre o nariz e queixo 3: "))

p1 = o1 / n1
p2 = o2 / n2
p3 = o3 / n3
if(abs(p1 - p2) < abs(p2 - p3) < abs(p3 - p1)):
	print("1 e 2")
elif(abs(p3 - p2) < abs(p1 - p3) < abs(p2 - p1)):
	print("2 e 3")
elif(abs(p1 - p3) < abs(p2 - p3) < abs(p2 - p1)):
	print("1 e 3")
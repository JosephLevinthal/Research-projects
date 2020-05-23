from math import*
x1=float(input("olhos imagem 1: "))
x2=float(input("nariz queixo imagem1: "))
y1=float(input("olhos imagem2: "))
y2=float(input("nariz queixo imagem2:"))
z1=float(input("olhos imagm 3 :"))
z2=float(input("nariz queixo imgaem 3: "))
p1=x1/x2
p2=y1/y2
p3=z1/z2
if(abs(p1-p2))<(abs(p1-p3)):
	print("1 e 2")
elif(abs(p1-p3))<(abs(p1-p2)):
	print("1 e 3")
elif(abs(p3-p2))<(abs(p3-p1)):
	print("2 e 3")

	
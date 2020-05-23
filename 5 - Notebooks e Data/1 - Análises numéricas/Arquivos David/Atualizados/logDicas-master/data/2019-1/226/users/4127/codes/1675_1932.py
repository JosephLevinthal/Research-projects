from math import*

o1= float(input("qual a distancia entre os olhos da imagem 1? "))
n1= float(input("qual a distancia entre o nariz e o queixo da imagem 1? "))
o2= float(input("qual a distancia entre os olhos da imagem 2? "))
n2= float(input("qual a distancia entre o nariz e o queixo da imagem 2? "))
o3= float(input("qual a distancia entre os olhos da imagem 3? "))
n3= float(input("qual a distancia entre o nariz e o queixo da imagem 2? "))

#calculando a razao das faces
p1= o1/n1
p2= o2/n2
p3= o3/n3

if (p3<p1<p2):
	print("1 e 3")
elif(p1<p3<p2):
	print("1 e 3")
elif(p1<p2<p3):
	print("1 e 2")
elif(p3<p2<p1):
	print("2 e 3")
elif(p2<p1<p3):
	print("1 e 2")
elif(p2<p3<p1):
	print("2 e 3")
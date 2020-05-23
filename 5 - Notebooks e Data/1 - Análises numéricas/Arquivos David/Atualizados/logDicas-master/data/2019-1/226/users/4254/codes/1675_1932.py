d1=float(input("Digite a distancia entre os olhos da imagem 1: "))
D1=float(input("Digite a distancia entre o nariz e queixo da imagem 1: "))
d2=float(input("Digite a distancia entre os olhos da imagem 2: "))
D2=float(input("Digite a distancia entre o nariz e queixo da imagem 2: "))
d3=float(input("Digite a distancia entre os olhos da imagem 3: "))
D3=float(input("Digite a distancia entre o nariz e queixo da imagem 3: "))

from math import*
p1=d1/D1
p2=d2/D2
p3=d3/D3

f1=abs(p1-p2)
f2=abs(p1-p3)
f3=abs(p2-p3)
if(f1<f2 and f1<f3):
	print("1 e 2")
elif(f2<f1 and f2<f3):
	print("1 e 3")
elif(f3<f1 and f3<f2):
	print("2 e 3")
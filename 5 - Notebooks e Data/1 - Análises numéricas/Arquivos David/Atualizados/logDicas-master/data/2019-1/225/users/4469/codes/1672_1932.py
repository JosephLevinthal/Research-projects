a1 = float(input("Distancia entre os olhos da imagem 1: "))
b1 = float(input("Distancia entre o nariz e queixo da imagem 1: "))
a2 = float(input("Distancia entre os olhos da imagem 2: "))
b2 = float(input("Distancia entre o nariz e queixo da imagem 2: "))
a3 = float(input("Distancia entre os olhos da imagem 3: "))
b3 = float(input("Distancia entre o nariz e queixo da imagem 3: "))

p1 = a1 / b1
p2 = a2 / b2
p3 = a3 / b3

menor_diferença = min(abs(p1 - p2), abs(p1 - p3), abs(p2 - p3))

if(menor_diferença == abs(p1 - p2)):
	print(str(1) + " e " + str(2))
elif(menor_diferença == abs(p1 - p3)):
	print(str(1) + " e " + str(3))
else:
	print(str(2) + " e " + str(3))
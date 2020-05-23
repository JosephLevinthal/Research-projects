a = float(input("Distancia entre os olhos, da imagem 1: "))
a1 = float(input("Distancia entre o nariz e o queixo, da imagem 1: "))
b = float(input("Distancia entre os olhos, da imagem 2: "))
b1 = float(input("Distancia entre o nariz e o queixo, da imagem 2: "))
c = float(input("Distancia entre os olhos, da imagem 3: "))
c1 = float(input("Distancia entre o nariz e o queixo, da imagem 3: "))

face1 = (a/a1)
face2 = (b/b1)
face3 = (c/c1)

if(face1 - face3 < face1 - face2 or face2 - face3):
	print("1 e 3")
elif(face2 - face3 < face1 - face2 or face1 - face3):
	print("2 e 3")
elif(face1 - face2 < face1 - face2 or face2 - face3):	
	print("1 e 2")

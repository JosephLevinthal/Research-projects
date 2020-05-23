a = float(input("distancia entre os olhos, da imagem 1:"))
a1= float(input("distancia entre o nariz e o queixo, da imagem 1:"))
b = float(input("distancia entre os olhos, da imagem 2:"))
b1 = float(input("distancia entre o nariz e o queixo, da imagem 2:"))
c = float(input("distancia entre os olhos, da imagem 3:"))
c1 = float(input("distancia entre o nariz e o queixo, da imagem 3:"))

f1 = a / a1
f2 = b / b1
f3 = c / c1

#calculo das faces

F1 = abs(f1 - f2)
F2 = abs(f1 - f3)
F3 = abs(f2 - f3)
if(F1 > F2):
	print(1, "e",3)
elif(F1 > F3):
	print(2, "e",3)
elif(F2 > F1):
	print(1, "e",2)
elif(F2 > F3):
	print(2, "e",3)
elif(F3 > F1):
	print(1, "e",2)
else:
	print(1, "e",3)

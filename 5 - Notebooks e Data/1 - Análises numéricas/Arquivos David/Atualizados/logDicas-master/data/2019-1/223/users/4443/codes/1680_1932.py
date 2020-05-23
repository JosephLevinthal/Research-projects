#coleta das caracteristicas:
a = float(input("distancia entre os olhos, da Imagem 1: "))
b = float(input("distancia entre  o nariz e o queixo, da Imagem 1: "))
c = float(input("distancia entre os olhos, da Imagem 2: "))
d = float(input("distancia entre  o nariz e o queixo, da Imagem 2: "))
e = float(input("distancia entre os olhos, da Imagem 3: "))
f = float(input("distancia entre  o nariz e o queixo, da Imagem 3: "))

f1 = round(a/b, 2)
f2 = round(c/d, 2)
f3 = round(e/f, 2)

f12 = abs(f1-f2)
f13 = abs(f1-f3)
f23 = abs(f2-f3)

if(f12 < f13) and (f12 < f23):
	print(1,"e", 2)
elif(f13 < f12) and (f13 < f23):
	print(1,"e", 3)
else:
	print(2,"e", 3)
	

a= float(input("distancia entre os olhos, da Imagem 1"))
b= float(input("distancia entre o nariz e o queixo, da Imagem 1"))
c=float(input("distancia entre os olhos, da Imagem 2"))
d=float(input("distancia entre o nariz e o queixo, da Imagem 2"))
e=float(input("distancia entre os olhos, da Imagem 3"))
f=float(input("distancia entre o nariz e o queixo, da Imagem 3"))
f1= a/b
f2= c/d
f3= e/f
k= abs(f1-f2)
j= abs(f1-f3)
s= abs(f2-f3)

if(k<j and k<s):
	print("1 e 2")
elif(j<k and j<s):
	print("1 e 3")
elif(s<k and s<j):
	print("2 e 3")
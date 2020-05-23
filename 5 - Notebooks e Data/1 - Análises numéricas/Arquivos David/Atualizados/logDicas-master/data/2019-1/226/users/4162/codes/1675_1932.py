a= float(input("distancia entre os olhos, da Imagem 1: "))
b= float(input("distancia entre o nariz e o queixo, da Imagem 1: "))
c= float(input("distancia entre os olhos, da Imagem 2: "))
d= float(input("distancia entre o nariz e o queixo, da Imagem 2: "))
e= float(input("distancia entre os olhos, da Imagem 3: "))
f= float(input("distancia entre o nariz e o queixo, da Imagem 3: "))
p1=(a/b)
p2=(c/d)
p3=(e/f)
s1=abs(p1-p2)
s2=abs(p1-p3)
s3=abs(p2-p3)
if (s2<s1)and(s2<s3):
	print("1 e 3")
elif (s1<s2)and(s1<s3):
	print("1 e 2")
elif (s3<s1)and(s3<s2):
	print("2 e 3")

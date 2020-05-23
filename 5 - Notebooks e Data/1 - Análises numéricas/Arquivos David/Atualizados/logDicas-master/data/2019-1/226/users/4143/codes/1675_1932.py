a = float(input("Distancia dos olhos 1:"))
b = float(input("Distancia entre o narize o queixo 1:"))
c = float(input("Distancia dos olhos 2:"))
d =  float(input("Distancia entre o nariz e o queixo 2:"))
e = float(input("Distancia dos olhos 3:"))
f=  float(input("Distancia entre o narize o queixo 3:"))
eq1=(a/b)
eq2=(c/d)
eq3=(e/f)
if ((abs(eq1-eq2))<(abs(eq2-eq3))):
	print("1 e 2")
elif(abs(eq1-eq3)<(abs(eq2-eq3))):
	print("1 e 3")
else:
	print("2 e 3")
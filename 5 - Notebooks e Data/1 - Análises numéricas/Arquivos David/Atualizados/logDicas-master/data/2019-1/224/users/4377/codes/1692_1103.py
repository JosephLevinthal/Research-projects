x=float(input("x"))
a=float(input("a"))
b=float(input("b"))

if(x>=a) and (x<=b):
	print(x,"pertence ao intervalo", a, "," , b)
elif(b<=a):
	print("Entradas",a, "e" , b, "invalidas")	
else:
	print(x, "nao pertence ao intervalo", a, "," , b)

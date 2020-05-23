x= float(input("Insira o numero de x:"))
a= float(input("Insira o primeiro intervalo:"))
b= float(input("Insira o segundo intervalo:"))

if (x>=a and x<=b):
	print(x," pertence ao intervalo ", a,", ",b)

elif (b<=a):
	print("Entradas ",a," e ",b," invalidas")

else:
	print(x," nao pertence ao intervalo ", a,", ",b)
	
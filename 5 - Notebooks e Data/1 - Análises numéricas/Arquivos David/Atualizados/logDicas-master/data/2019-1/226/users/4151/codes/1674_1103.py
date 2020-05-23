x=float(input("num1: "))
a=float(input("num2: "))
b=float(input("num3: "))

if(b<=a):
	print("Entradas" , a, "e" , b, "invalidas")
elif(a<=x)and(x<=b):
	print(x, "pertence ao intervalo" , a,",", b)
elif(x<=a)or(x>=b):
	print(x, "nao pertence ao intervalo" , a,",", b)

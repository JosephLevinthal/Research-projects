x = float(input("digite x: "))
a = float(input("digite a: "))
b = float(input("digite b: "))

if ((a < x) and  (x < b)):
	print(x, "pertence ao intervalo", a ,",", b)
elif (b <= a):
	print("Entradas",a ,"e", b, "invalidas")
else:
	print(x, "nao pertence ao intervalo" ,a ,",", b)

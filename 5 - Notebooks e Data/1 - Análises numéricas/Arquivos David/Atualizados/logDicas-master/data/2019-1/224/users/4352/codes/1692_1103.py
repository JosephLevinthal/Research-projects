x = float(input("digite x: "))
a = float(input("digite a: "))
b = float(input("digite b: "))

if a <= x <= b and b>a:
	print(x,"pertence ao intervalo",a,",",b)
elif not(a <= x <= b) and b>a:
	print(x," nao pertence ao intervalo",a,",",b)
else:
	print("Entradas",a,"e",b,"invalidas")



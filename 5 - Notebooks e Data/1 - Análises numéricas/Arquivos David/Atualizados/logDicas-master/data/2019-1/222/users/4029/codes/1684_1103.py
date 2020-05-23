x = float(input("Digite um numero x: "))
y = float(input("Valor 'a' do intervalo fechado [a,b]: "))
z = float(input("Valor 'b' do intervalo fechado [a,b]: "))

if (z > y):
	if (x >= y) and (x <= z):
		print(x, "pertence ao intervalo", y, ",", z)
	else:  
		print(x, "nao pertence ao intervalo", y, ",", z)
else:
	print("Entradas", y, "e", z, "invalidas")

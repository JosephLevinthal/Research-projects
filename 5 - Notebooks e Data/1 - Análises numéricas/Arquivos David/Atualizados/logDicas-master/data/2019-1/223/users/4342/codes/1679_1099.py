x=float(input("numero:"))
y=float(input("numero:"))
z=float(input("numero:"))

a="equilatero"
b="isosceles"
c="escaleno"
d="invalido"
if(x == y) and (y == z):
	print("Tipo de triangulo:",a)
elif((var==var2) and (var!=var3)):
	print("Tipo de triangulo:",b)
elif((var!=var2) or (var2!=var3)):
	print("Tipo de triangulo:",c)
elif((x >= y + z) or (y >= z + x) or (z >= x + y)):
		print("Tipo de triangulo:",d)
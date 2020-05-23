a= float(input("lado a: "))
b= float(input("lado b: "))
c= float(input("lado c: "))
print("Entradas:", a,",", b,",", c)

if ((a< b+c and b< a+c and c< a+b) and a>=0 and b>=0 and c>=0):
	if (a==b and b==c):
		print("Tipo de triangulo: equilatero")
	else:
		if (a!=b and b!=c and c!=a):
			print("Tipo de triangulo: escaleno")
		else:
			print("Tipo de triangulo: isosceles")
else:
	print("Tipo de triangulo: invalido")
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))
x = "Tipo de triangulo:"
	
print("Entradas:", a, ",", b, ",", c)
if((a>=b+c)or(b>=a+c)or(c>=a+b)):
	print(x,"invalido")
else:
	if((a==b)and(b==c)):
		print(x,"equilatero")
	elif((a==b)or(b==c)or(c==a)):
		print(x,"isosceles")
	else:
		print(x,"escaleno")

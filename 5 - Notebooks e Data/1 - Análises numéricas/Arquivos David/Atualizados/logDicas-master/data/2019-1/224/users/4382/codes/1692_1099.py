a = float(input ("digite a: "))
b = float(input ("digite b: "))
c = float(input ("digite c: "))
print("Entradas:", a, ",", b, ",", c)
if (a>0 and b>0 and c>0):
	if(a<b+c and b<a+c and c<a+b):
		if(a==b==c):
			print("Tipo de triangulo: equilatero")
		elif(a!=b!=c):
			print("Tipo de triangulo: escaleno")
		else:
			print("Tipo de triangulo: isosceles")
	else:
			print("Tipo de triangulo: invalido")
else:
			print("Tipo de triangulo: invalido")
	

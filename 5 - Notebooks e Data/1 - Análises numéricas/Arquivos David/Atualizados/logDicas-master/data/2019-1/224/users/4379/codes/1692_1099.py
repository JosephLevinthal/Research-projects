a=float(input(" entrada a:"))
b=float(input(" entrada b:"))
c=float(input(" entrada c:"))
print("Entradas:", a,",", b,",",c)
if(a>0 and b>0 and c>0):
	if(abs(b-c)< a < b or abs(a-c)< b < a + c or abs(a-b) < c < a+b):
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
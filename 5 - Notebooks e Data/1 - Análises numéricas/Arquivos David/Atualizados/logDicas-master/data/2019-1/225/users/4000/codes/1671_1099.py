a = float(input("Lado x: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))
print("Entradas:",a,",", b,"," , c)
if(a<=0) or (b<=0) or (c <= 0):
	print("Tipo de triangulo: invalido")
else:
	if(a>b+c)or (b>=c+a)or (c>=a+b):
		print("Tipo de triangulo: invalido")
	elif ((a==b) and (b==c)and (c==a)):
		print("Tipo de triangulo: equilatero")
	elif(a==b) or (a==c) or (c==b):
		print("Tipo de triangulo: isosceles")
	elif(a!=b) and (b!=c) and (c!=a):
		print("Tipo de triangulo: escaleno")
	

	
		

	

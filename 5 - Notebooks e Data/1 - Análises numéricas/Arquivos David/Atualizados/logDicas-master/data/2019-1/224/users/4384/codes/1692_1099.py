a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))
print("Entradas: ",a, ", ",b, ", ",c)
if(a<b+c)and(c<a+b)and(b<c+a):
	if((a==b) and (b==c)):
		print("Tipo de triangulo: equilatero")
	elif(a==b)or(b==c)or(c==a):
		print("Tipo de triangulo: isosceles")
	elif(a!=b)and(b!=c)and(c!=a):
		print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")
	
		


a=float(input("digite o lado a:"))
b=float(input("digite o lado b:"))
c=float(input("digite o lado c:"))
print("Entradas:", a, ",", b, ",", c)
if(a<b+c and b<c+a and c<a+b):
	if a==b and b==c and a<=0:
		print("Tipo de triangulo: equilatero")
	elif(a==b or b==c or a==c):
		print ("Tipo de triangulo: isosceles")
	elif(a!=b or a!=c or c!=b):
		print ("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")
		

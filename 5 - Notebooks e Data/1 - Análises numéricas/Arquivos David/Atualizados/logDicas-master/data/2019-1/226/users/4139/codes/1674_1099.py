a = float(input("valor de a:"))
b = float(input("valor de b:"))
c = float(input("valor de c:"))
h = "Tipo de triangulo: "

print("Entradas:", a,",", b,",",c)
if(a<b+c)and(b<a+c)and(c<a+b):
	if(a == b) and (b == c):
		print(h,"equilatero")
	elif(a==b) or (b==c) or (a==c):
		print(h,"isosceles")
	elif(a!=b) and (b!=c) and (a!=c):
		print(h,"escaleno")
else:
	print("Tipo de triangulo: invalido")
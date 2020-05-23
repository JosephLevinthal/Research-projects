a=float(input("digite a: "))
b=float(input("digite b: "))
c=float(input("digite c: "))
print("Entradas: ", a, ",", b, "," , c)
if(a< b+c) and (b< c+a) and (c< a+b):
	if a==b and b==c and a<=0 :
		print("Tipo de triangulo: equilatero")
	elif a==b or a==c or b==c:
		print("Tipo de triangulo: isosceles")
	elif a!=b and a!=c and b!=c:
		print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")
a = float(input("digite o n1: "))
b = float(input("digite o n2: "))
c = float(input("digite o n3: "))
print("Entradas:", a,",", b,",",c)
if((a<=0) or (b<=0) or (c<=0)) or ((a>=b+c) or (b>=a+c)or(c>=a+b)):
	print("Tipo de triangulo: invalido")
elif(a == b) and (c == b) and (a == c):
	print("Tipo de triangulo: equilatero")
elif(a==b) or (a==c) or (c==b):
	print("Tipo de triangulo: isosceles")
elif(a!=b) and (b!=c) and (a!=c):
	print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")


	
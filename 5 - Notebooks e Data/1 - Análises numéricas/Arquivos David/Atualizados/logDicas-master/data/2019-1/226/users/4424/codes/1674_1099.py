A = float(input ("Lado 1: "))
B = float(input ("Lado 2: "))
C = float(input ("Lado 3: "))

print("Entradas:", A, ",", B, ",", C)
if(A<B+C)and(B<A+C)and(C<A+B):
	if(A==B)and(B==C):
		print("Tipo de triangulo: equilatero")
	elif(A==B)and(B!=C)or(B==C)and(B!=A)or(A==C)and(C!=B):
		print("Tipo de triangulo: isosceles")
	else:
		print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")
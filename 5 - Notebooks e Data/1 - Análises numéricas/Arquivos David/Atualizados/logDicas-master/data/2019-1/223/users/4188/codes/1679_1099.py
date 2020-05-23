# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
A=float(input("L1: "))
B=float(input("L2: "))
C=float(input("L3: "))
print("Entradas:", A, ",", B, ",", C)
if(A>0 and B>0 and C>0):
	if (A+B>C and A+C>B and B+C>A):
		if( A==B and B==C):
			print("Tipo de triangulo: equilatero")
		if ((A==B and B!=C) or (A!=B and B==C)):
			print("Tipo de triangulo: isosceles")
		if (A!=B and B!=C):
			print("Tipo de triangulo: escaleno")
	if (A+B<C or A+C<B or B+C<A):
			print("Tipo de triangulo: invalido")
else:
	print("Tipo de triangulo: invalido")
			
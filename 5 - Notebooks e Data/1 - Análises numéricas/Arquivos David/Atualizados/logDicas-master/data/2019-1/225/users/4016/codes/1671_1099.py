# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
A= float(input("Lado A : "))
B= float(input("Lado B : "))
C= float(input("Lado C : "))

print("Entradas: ", A,",",B,",",C) 

if ((A>=B+C) or (B>=A+C) or (C>=B+A)):
	print("Tipo de triangulo: invalido")
else:
	if((A==B)and (B==C)and (C==A)) :
		print("Tipo de triangulo: equilatero")
	else:
		if(A==B) or (B==C):
			print("Tipo de triangulo: isosceles")
		if((A!=B) and (B!=C)):
				print("Tipo de triangulo: escaleno")
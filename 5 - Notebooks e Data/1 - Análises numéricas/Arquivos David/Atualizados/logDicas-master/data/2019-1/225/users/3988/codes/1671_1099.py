# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
A = float(input("A:"))
B = float(input("B:"))
C = float(input("C:"))
print("Entradas: ", A,",", B,",", C)
if ((C>=A+B) or (B>=C+A) or (A>=C+B)):
	print("Tipo de triangulo: invalido")
elif ((A==B) and (B==C)):
	print("Tipo de triangulo: equilatero")
elif ((A==B) or (A==C) or (B==C)):
	print("Tipo de triangulo: isosceles")
else:
	print("Tipo de triangulo: escaleno")
	
	
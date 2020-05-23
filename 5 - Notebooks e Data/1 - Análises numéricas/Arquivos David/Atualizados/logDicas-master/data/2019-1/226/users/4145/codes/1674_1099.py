# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
A = float(input("cumprimento de A:"))
B = float(input("cumprimento de B:"))
C = float(input("cumprimento de C:"))
if((A < B + C)and(C < A + B)and(B < A + C)):
	
	if( A == B == C ):
		tt = "equilatero"
	elif((A==B!=C)or(B==C!=A)or(A==C!=B)):
		tt = "isosceles"
	elif(A != B != C):
		tt = "escaleno"
else:
	tt = "invalido"
print("Entradas:" ,A,"," ,B ,",", C)
print("Tipo de triangulo:", tt)
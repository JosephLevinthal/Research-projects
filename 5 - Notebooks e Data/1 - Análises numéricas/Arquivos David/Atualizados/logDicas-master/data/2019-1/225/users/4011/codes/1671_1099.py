# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

A= float(input("Lado a: "))
B= float(input("Lado b: "))
C= float(input("Lado c: "))

print("Entradas:", A, ",", B, ",", C)

if( (A > 0) or (B > 0) or (C > 0) ):
	if( (A < B + C) and (B < A + C) and (C < A + B) ):
		if (( A == B ) and ( B == C)):
			print("Tipo de triangulo: equilatero")
		elif( A == B ) or ( B == C ) or ( A == C):
			print("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: escaleno")
	else:
		print("Tipo de triangulo: invalido" )
else:
	print("Tipo de triangulo: invalido" )
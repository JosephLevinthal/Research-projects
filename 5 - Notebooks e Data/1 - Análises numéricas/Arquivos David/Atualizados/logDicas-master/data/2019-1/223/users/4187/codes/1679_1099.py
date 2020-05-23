# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
A = float(input("lado A:"))
B = float(input("lado B:"))
C = float(input("lado C:"))
 
if( A <= 0 or B <= 0 or C <= 0 ):
	print("Entradas:",A,",",B,",",C)
	print("Tipo de triangulo:","invalido")
elif((A >= B + C) or (B >= A + C) or (C >= B + A)):
	print("Entradas:",A,",",B,",",C)
	print("Tipo de triangulo:","invalido")
	
elif((A == B) and (B == C)):
	print("Entradas:",A,",",B,",",C)
	print("Tipo de triangulo:","equilatero")
elif((A == B) or (B == C) or (C == A)):
	print("Entradas:",A,",",B,",",C)
	print("Tipo de triangulo:","isosceles")
elif((A != B) and (B != C) and (C != A) ):
	print("Entradas:",A,",",B,",",C)
	print("Tipo de triangulo:","escaleno")

	
	
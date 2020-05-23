# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
A = float(input("lado a"))
B = float(input("lado b"))
C = float(input("lado c"))
print("Entradas:", A, ",", B, ",", C)
if ((A >= B + C) or(B >= C + A) or(C >= A + B)):
	print("Tipo de triangulo: invalido")
else:
		if ((A == B) and (B == C)):
			print("Tipo de triangulo: equilatero")
		else:
			if ((A == B) or(B == C) or(C == A)):
				print("Tipo de triangulo: isosceles")
			else:
				print("Tipo de triangulo: escaleno")
		
	


		
	
 

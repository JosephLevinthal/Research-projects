# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
A = float(input("lado: "))
B = float(input("lado: "))
C = float(input("lado: "))
print("Entradas:", A, ",", B, ",", C)
if ((A!=0)and(B!=0)and(C!=0)):
	if((A>=B+C) or (B>=A+C) or (C >= B + A)):
		x = "invalido"
	else:
		if((A == B) and (B == C)):
			x = "equilatero"
		if((A == B) or (B == C) or (C == A)):
			x = "isosceles"	
		else:
			x = "escaleno"
else:
	x="invalido"

print("Tipo de triangulo: "+ x)
# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
A = float(input(" Digite lado 1: "))
B = float(input(" Digite lado 2: "))
C = float(input(" Digite lado 3: "))
print("Entradas:", A, ",", B, ",", C)
if((A<0) and (B<0) and (C<0)):
	print(" Tipo de triangulo: invalido ")

else:
	if((A>=B+C) or (B>=A+C) or (C>=A+B)):
		mensagem = " invalido "
	else:
		if((B==C) and (C==A)):
			mensagem = " equilatero "
		else:
			if((A==B) or (B==C) or (C==A)):
				mensagem = " isosceles "
			else:
				mensagem = " escaleno "
print(" Tipo de triangulo: ", mensagem)
		
# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("lado a:"))
b = float(input("lado b:"))
c = float(input("lado c:"))

print( "Entradas:" , a , "," , b , "," , c)

if ((a < b + c) and (b < c + a) and (c < a + b)):
	
	if((a == b) and (b == c) and (a == c)):
		print("Tipo de triangulo: equilatero")
	else:
		if((a == b) or (b == c) or (c == a)):
			print("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")
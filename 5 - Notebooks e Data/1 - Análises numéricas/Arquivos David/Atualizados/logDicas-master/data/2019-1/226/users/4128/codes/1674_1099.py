# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a= float(input (" 1: "))
b= float(input (" 2: "))
c= float(input (" 3: "))

print("Entradas:", a,"," , b, ",", c)

if((a < b + c) and (b < c + a) and (c < b + a)):
	if((a ==  b) and (b == c) and (a == c)):
		print("Tipo de triangulo: equilatero")
	else:
		if((a == b) or (b == c)):
			print("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")
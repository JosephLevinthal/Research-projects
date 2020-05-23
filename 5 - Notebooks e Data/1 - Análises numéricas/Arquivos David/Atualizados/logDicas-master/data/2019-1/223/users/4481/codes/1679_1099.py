# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("insira um valor a: "))
b = float(input("insira um valor b: "))
c = float(input("insira um valor c: "))

print("Entradas:",a, ",", b, ",", c)

if((a>= b + c) or (b>= a + c) or (c>= b + a)):
	print("Tipo de triangulo: invalido")
else:
	if((a==b) and (b==c)):
		print("Tipo de triangulo: equilatero")
	else:
		if((a==b) or (b==c) or (c==a)):
			print("Tipo de triangulo: isosceles")
		else:
			if((a != b) and (b != c) and(c != a)):
				print("Tipo de triangulo: escaleno")
			else:
				print("Tipo de triangulo: invalido")

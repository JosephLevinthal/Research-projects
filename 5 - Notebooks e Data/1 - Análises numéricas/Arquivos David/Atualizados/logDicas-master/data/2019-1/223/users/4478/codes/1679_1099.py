# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input ("A: "))
b = float(input("B: "))
c = float(input("C: "))

if((a>=b+c)or(b>=a+c)or(c>=a+b)):
	print("Entradas:", a, ",", b, ",", c)
	print("Tipo de triangulo: invalido")
else:
	if((a==b)and(b==c)):
		print("Entradas:", a, ",", b, ",", c)
		print("Tipo de triangulo: equilatero")
	else:
		if((a==b)or(b==c)or(c==a)):
			print("Entradas:", a, ",", b, ",", c)
			print("Tipo de triangulo: isosceles")
		else:
			print("Entradas:", a, ",", b, ",", c)
			print("Tipo de triangulo: escaleno")
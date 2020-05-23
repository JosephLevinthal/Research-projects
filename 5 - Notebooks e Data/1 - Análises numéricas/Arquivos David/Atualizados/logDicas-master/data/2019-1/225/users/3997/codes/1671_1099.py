# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
lado1 = float(input("Digite um numero: "))
lado2 = float(input("Digite um numero: "))
lado3 = float(input("Digite um numero: "))
print("Entradas:", lado1, ",",lado2, ",", lado3 )

if ((lado1 >= lado2 + lado3) or (lado2 >= lado1 + lado3) or (lado3 >= lado1 + lado2)):
	print("Tipo de triangulo:" " invalido")
else:
	if((lado1 == lado2) and (lado1 == lado3) and (lado2 == lado3)):
		print("Tipo de triangulo:" " equilatero")
	else:
		if((lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3)):
			print("Tipo de triangulo:" " isosceles")
		else:
			print("Tipo de triangulo:" " escaleno")
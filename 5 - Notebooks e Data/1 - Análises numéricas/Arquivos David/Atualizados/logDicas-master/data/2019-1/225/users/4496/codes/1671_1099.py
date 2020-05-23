# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = float(input("Digite o lado A: "))
y = float(input("Digite o lado B: "))
z = float(input("Digite o lado C: "))

print("Entradas:", x , ",", y , "," , z)

if(abs(y-z)<x<(y+z)):
	if((x == y) and (y == z) and (x == z)):
		print ("Tipo de triangulo:" , "equilatero")
	else:
		if((x == y) or (y == z)):
			print("Tipo de triangulo:" , "isosceles")
		else:
			print("Tipo de triangulo:" , "escaleno")
else:
	print("Tipo de triangulo:" , "invalido")
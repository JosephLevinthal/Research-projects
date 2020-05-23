# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de 
x = float(input("valor de X? "))
y = float(input("valor de Y? "))
z = float(input("valor de Z? "))
print("Entradas:", x, ",", y, ",", z)

if (x < y + z) and (y < x + z) and (z < x + y):
	if ((x != y) and (y != z) and (z != x)):
		print("Tipo de triangulo: escaleno")
	else:
		if ((x != y) or (y != z)):
			print("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: equilatero")
else:
	print("Tipo de triangulo: invalido")
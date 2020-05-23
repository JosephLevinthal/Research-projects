# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades 
x=float(input(""))
y=float(input(""))
z=float(input(""))
print("Entradas:" , x,",",y,",",z)
if ((x >= y + z)) or ((y >= x + z)) or ((z >= y + x)):
	print("Tipo de triangulo: invalido")
	
else:
	if ((x == y)) and ((y == z)):
		print("Tipo de triangulo: equilatero")
	else:
		if ((x == y)) or ((y == z)) or ((z == x)):
		   print("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: escaleno")
		
# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = float(input("lado 1: "))
y = float(input("lado 2: "))
z = float(input("lado 3: "))

print("Entradas:",x,",",y,",",z)
if(x < 0 ) or (y < 0) or (z < 0):
	tipo = "invalido"
elif(x >= y + z) or (y >= x + z) or (z >= x + y):
	tipo = "invalido"
else:
	if((x == y) and (y == z)):
		tipo = "equilatero"
	else:
		if(x == y) or (x == z) or (y == z):
			tipo = "isosceles"
		else:
			tipo = "escaleno"

print("Tipo de triangulo:",tipo)

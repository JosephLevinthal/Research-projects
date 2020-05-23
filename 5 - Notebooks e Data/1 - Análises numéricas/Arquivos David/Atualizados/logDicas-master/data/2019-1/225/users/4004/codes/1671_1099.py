# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("lado ab: "))
b = float(input("lado bc: "))
c = float(input("lado ca: "))

print("Entradas: ", a,",", b,",", c)

if a > 0 or b > 0 or c > 0:
	if a < b + c and b < a + c and c < a + b:
		if a == b and b == c:
			x = "equilatero"
		elif a == b or a == c or b == c:
			x = "isosceles"
		else:
			x = "escaleno"
	else:
		x = "invalido"
else:
	x = "invalido"
			
print("Tipo de triangulo: ", x)
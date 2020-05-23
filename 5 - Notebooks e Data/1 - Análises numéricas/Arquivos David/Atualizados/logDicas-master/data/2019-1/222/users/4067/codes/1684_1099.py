# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))
print("Entradas: ",a ,",",b,",",c)
if a > 0 and b > 0 and c > 0:
	if a < b+c and c < b+a and b < a+c:
		if a==b and b==c:
			print("Tipo de triangulo: equilatero")
		elif a==b or a==c or c==b:
			print("Tipo de triangulo: isosceles")
		elif a != b and b != c and c != a:
			print("Tipo de triangulo: escaleno")
	else:
			print("Tipo de triangulo: invalido")
else:
	print("tipo de triangulo: invalido")
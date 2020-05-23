# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("lado 1:"))
b = float(input("lado 2:"))
c = float(input("lado 3:"))

print("Entradas:", a, ",", b, ",", c)
if ((a+b >c) and (b+c > a) and (c+a > b)):
	if (a == b) and (b == c):
		print("Tipo de triangulo: equilatero")
	elif (a == b) or (b == c) or (c == a):
		print("Tipo de triangulo: isosceles")
	else:
		print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")
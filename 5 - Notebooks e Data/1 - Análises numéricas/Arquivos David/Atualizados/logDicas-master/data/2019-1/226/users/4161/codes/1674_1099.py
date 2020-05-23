# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))
print("Entradas: ", a, "," , b, ",", c)
if (a< c+b) and (b< c+a) and (c< a+b):
	if (a==b==c):
		x = "equilatero"
	elif (a==b) or (b==c) or (a==c):
		x = "isosceles"
	elif (a!=b) and (a!=c) and (c!=b):
		x = "escaleno"
else:
	x = "invalido"
print("Tipo de triangulo:", x)
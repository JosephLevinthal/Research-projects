# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("digite o lado a: "))
b = float(input("digite o lado b: "))
c = float(input("digite o lado c: "))

if(a<(b+c) and b<(a+c) and c<(b+a)):
	if(a==b and b==c and c==a):
		print("Entradas:", a, ",", b, ",", c)
		print("Tipo de triangulo: equilatero")
	elif(a==b or b==c or c==a):
		print("Entradas:", a, ",", b, ",", c)
		print("Tipo de triangulo: isosceles")
	else:
		print("Entradas:", a, ",", b, ",", c)
		print("Tipo de triangulo: escaleno")
	
else:
	print("Entradas:", a, ",", b, ",", c)
	print("Tipo de triangulo: invalido")

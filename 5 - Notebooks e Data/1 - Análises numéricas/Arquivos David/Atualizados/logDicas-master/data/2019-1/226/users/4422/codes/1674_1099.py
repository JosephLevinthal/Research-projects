# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))

print("Entradas:" , a, ",", b, ",", c)


if( a<b+c and b<c+a and c<b+a):
	if(a==b and b == c):
		print("Tipo de triangulo: equilatero")
	elif(a==b and b!=c or b==c and b!=a):
		print("Tipo de triangulo: isosceles")
	else:
		print("Tipo de triangulo: escaleno")
		
else:
	print("Tipo de triangulo: invalido")

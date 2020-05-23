# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))
c = float(input("Digite um numero: "))

print("Entradas:", a, ",", b, ",", c )

if(a < b + c and b < a + c and c < a + b):
	print("Tipo de triangulo: ")
	if(a == b and b == c):
		print("equilatero")
	elif(a == b or b == c or c == a):
		print("isosceles")
	else:
		print("escaleno")
else:
	print("Tipo de triangulo:", "invalido")
	


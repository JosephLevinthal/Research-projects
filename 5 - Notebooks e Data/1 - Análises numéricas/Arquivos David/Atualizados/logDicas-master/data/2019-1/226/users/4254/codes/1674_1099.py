# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))

if(a < 0 or b < 0 or c < 0):
	print("Entradas:", a,"," ,b,",", c)
	print("Tipo de triangulo: invalido")
elif((a>=b+c) or (b>=a+c) or (c>=a+b)):
	print("Entradas:", a,"," ,b,",", c)
	print("Tipo de triangulo: invalido")
elif(a==b and a==c):
	print("Entradas:", a,"," ,b,",", c)
	print("Tipo de triangulo: equilatero")
elif(a==b or a==c or b==c):
	print("Entradas:", a,"," ,b,",", c)
	print("Tipo de triangulo: isosceles")
else:
	print("Entradas:", a,"," ,b,",", c)
	print("Tipo de triangulo: escaleno")

		
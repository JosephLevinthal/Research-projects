# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = float(input("valor de x: "))
y = float(input("valor de y: "))
z = float(input("valor de z: "))

if ( x <= 0 or y <= 0 or z <=0 ):
	print("Entradas:",x,",",y,",",z)
	print("Tipo de triangulo:","invalido")
elif (( x >= y + z ) or ( y >= x + z) or ( z >= x + y)):
	print("Entradas:",x,",",y,",",z)
	print("Tipo de triangulo:","invalido")
elif (( x == y ) and ( y == z )):
	print("Entradas:",x,",",y,",",z)
	print("Tipo de triangulo:","equilatero")
elif (( x == y ) or ( y == z ) or ( z == x)):
	print("Entradas:",x,",",y,",",z)
	print("Tipo de triangulo:","isosceles")
elif (( x != y) and ( x != z ) and ( y != z )):
	print("Entradas:",x,",",y,",",z)
	print("Tipo de triangulo:","escaleno")


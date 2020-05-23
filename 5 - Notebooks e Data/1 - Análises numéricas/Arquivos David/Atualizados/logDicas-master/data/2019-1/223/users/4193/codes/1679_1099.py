# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

# Entrada de dados :
x = float(input("Lado x: "))
y = float(input("Lado y: "))
z = float(input("Lado z: "))
if ( x <=0 or y <=0 or z <=0 ):
   print ("Entradas: ",x,",",y,",",z)
   print ("Tipo de Triangulo:","invalido")
elif ((x >= y + z) or ( y >= x + z) or (z >= x + z )):
   print ("Entradas:",x,",",y,",",z)
	print ("Tipo de Triangulo:","invalido")
elif ( x == y) and ( y == z)
   print("Entradas:",x,",",y,",",z)
	print("Tipo de Triangulo:","equilatero")
elif ( x == y) or (y == z) or ( z == x):
   print(" Entradas:",x,",",y,",",z)
	print("Tipo de Triangulo","isosceles")
elif ( x != y) or ( x != z) or ( y != z):
   print("Entradas:",x,",",y,",",z)
	print("Tipo de Triangulo","escaleno")
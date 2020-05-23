a= float(input("Medida de a: "))
b= float(input("Medida de b: "))
c= float(input("Medida de c: "))
print('Entradas:' ,a, ',', b, ',', c)

if ((a >= b + c) or (b >= a + c) or (c >= a +b)):
	print('Tipo  de triangulo: invalido')
	
elif ((a == b) and (b == c)):
	print('Tipo  de triangulo: equilatero')
		
elif ((a == b) or (b == c)):
	print('Tipo  de triangulo: isosceles')
		
elif ((a != b) and (b != c) and (c != a)):
	print('Tipo  de triangulo: escaleno')
		
else:
	print('Tipo  de triangulo: invalido')
		
 

			
			
    


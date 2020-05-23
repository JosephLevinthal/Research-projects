# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("lado a:"))
b = float(input("lado b:"))
c = float(input("lado c:"))
print("Entradas:", a,",",b,",",c )
es = "escaleno"
i = "isosceles"
eq = "equilatero"
if((a > 0) and (b > 0)and (c > 0)):
	if(a < b +c) and (b < a + c) and (c < a + b):
		if( a == b) and (b == c):
			print("Tipo de triangulo:",eq)
		elif ((a == b) or (a == c) or (b == c)):
			print("Tipo de triangulo:",i )
		else:
			print("Tipo de triangulo:",es )
	else:
		print("Tipo de triangulo: invalido")
else:
	print("Tipo de triangulo: invalido")
			
	

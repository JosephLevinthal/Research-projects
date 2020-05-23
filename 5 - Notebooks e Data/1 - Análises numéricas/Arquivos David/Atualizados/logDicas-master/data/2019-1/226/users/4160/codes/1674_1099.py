# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = float(input("Lado1: "))
y = float(input("Lado2: "))
z = float(input("Lado3: "))

print("Entradas: " , x ,",", y ,",", z)

if (x>0 and y>0 and z>0):
	if (x < y + z and y < x + z and z < x + y):
		if(x==y and y==z):
			h = "equilatero"
			print("Tipo de triangulo:", h)
		elif(x==y and y!=z or z==y and z!=x):
			h = "isosceles"
			print("Tipo de triangulo:", h)
		else:
			h = "escaleno"
			print("Tipo de triangulo:", h)
	else:
		h = "invalido"
		print("Tipo de triangulo:", h)			
else:	
	print("Tipo de triangulo: invalido")
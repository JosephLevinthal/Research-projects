# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de sVR
a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))
print("Entradas:", a, ",", b, ",", c)

if (a>=b+c or b>=a+c or c>=a+b) or (a<0 or b<0 or c<0):
	print("Tipo de triangulo: invalido")

elif (a==b) and (b==c):
	print("Tipo de triangulo: equilatero")
	
elif (a==c) or (a==b) or (b==c):
	print("Tipo de triangulo: isosceles")
	
else:
	print("Tipo de triangulo: escaleno")
# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input ("Lado a: "))
b = float(input ("Lado b: "))
c = float(input ("Lado c: "))
print("Entradas:", a, ",", b, ",", c)
if ((a >= b + c) or (b >= a + c) or (c >= b + a)):
	print("Tipo de triangulo: invalido")
elif ((a == b) and (b == c)):
	print("Tipo de triangulo: equilatero")
elif ((a == b) or (b == c) or (c == a)):		
	print("Tipo de triangulo: isosceles")
else:	
	print("Tipo de triangulo: escaleno")

# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

a = float(input("numero 1: "))
b = float(input("numero 2: "))
c = float(input("numero 3: "))

print("Entradas:", a, ",", b, ",", c)

if ((a < 0) or (b < 0) or (c < 0)or (a + b <= c) or (b + c <= a) or (a + c <= b)):
	print ('Tipo de triangulo: invalido')
elif ((a==b and b==c)):
	print ("Tipo de triangulo: equilatero")
elif (a == b or b == c or c == a):
	print("Tipo de triangulo: isosceles")
else:
	print("Tipo de triangulo: escaleno")
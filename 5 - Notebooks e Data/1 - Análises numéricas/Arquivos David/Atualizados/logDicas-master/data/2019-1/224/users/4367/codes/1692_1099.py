# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a= float(input("escolha um numero: "))
b= float(input("escolha um numero: "))
c= float(input("escolha um numero: "))
print("Entradas:", a, ",", b, ",", c)
if (a< b+c) and (b< a+c) and (c< a+b):
	if a==b and b==c and a<=0:
		print("tipo de triangulo: equilatero")
	elif a==b or b==c or a==c:
		print("Tipo de triangulo: isosceles")
	elif a!=b and b!=c and c!=a:
		print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")
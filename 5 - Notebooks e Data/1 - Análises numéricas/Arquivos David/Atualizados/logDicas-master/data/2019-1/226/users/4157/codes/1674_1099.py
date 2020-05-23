# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("valor de a:"))
b = float(input("valor de b:"))
c = float(input("valor de c:"))
print("Entradas:",a,",",b,",",c)
if(a<b+c) and (b<c+a) and (c<a+b):
	if(a==b==c):
		print("Tipo de triangulo: equilatero")
	elif(a==b)or(a==c)or(b==c):
		print("Tipo de triangulo: isosceles")
	elif(a!=b!=c):
		print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")


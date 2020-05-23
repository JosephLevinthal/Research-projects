# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
print("Entradas:",a,",",b,",",c,)
if(a>=b+c) or (b>=c+a) or (c>=a+b):
	print("Tipo de triangulo: invalido")
elif(a==b)and (c==a):
	print("Tipo de triangulo: equilatero")
elif(a==b) or (b==c) or (a==c):
	print("Tipo de triangulo: isosceles")
else:
	print("Tipo de triangulo: escaleno")

	
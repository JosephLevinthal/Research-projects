# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a= float(input("lado1: "))
b=float(input("lado2: "))
c=float(input("lado3: "))

x= "Tipo de triangulo:"
print("Entradas:",a, ",",b,",",c)
if (a>=b+c or b>=a+c or c>=a+b or c<0 or b<0 or a<0):
	print(x,"invalido")
else:
	if(a==b and b==c):
		print(x,"equilatero")
	else:
		if(a==b or b==c or c==a):
			print(x,"isosceles")
		else:
			print(x,"escaleno")
			
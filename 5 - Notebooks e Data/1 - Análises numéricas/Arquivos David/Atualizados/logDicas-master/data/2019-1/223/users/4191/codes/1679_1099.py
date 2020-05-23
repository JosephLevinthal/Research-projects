# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a=float(input("Lado 1: "))
b=float(input("Lado 2: "))
c=float(input("Lado 3: "))
print("Entradas:" , a,",",b,",",c)
if ((a>=b+c)or(b>=a+c)or(c>=a+b)):
	print("Tipo de triangulo: invalido")
else:
	if((a==b)and(b==c)):
		print("Tipo de triangulo: equilatero")
	else:
		if((a == b)or(a == c)or(b == c)):
			print("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: escaleno")

			

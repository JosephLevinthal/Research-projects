# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a=float(input("lado 1: "))
b=float(input("lado 2: "))
c=float(input("lado 3: "))
if (a>=b+c)or(b>=a+c)or(c>=a+b):
	print("Entradas:" ,a, "," ,b, "," ,c)
	print("Tipo de triangulo: invalido")
else:
	print("Entradas:" ,a, "," ,b, "," ,c)
	if ((a==b==c)):
		print("Tipo de triangulo: equilatero")
	else:
		if (a!=b) and (a!=c) and (b!=c):
			print("Tipo de triangulo: escaleno")
		else:
			print("Tipo de triangulo: isosceles")
			
		
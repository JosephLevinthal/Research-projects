# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input('Insira um numero a: '))
b = float(input('Insira um numero b: '))
c = float(input('Insira um numero c: '))

print('Entradas:', a,',', b,',', c)

if ((c>=a+b) or (a>=b+c) or (b>=a+c)):
	print('Tipo de triangulo: invalido')
else:
	if ((a==b) and (b==c)):
		print('Tipo de triangulo: equilatero')
	else:
		if ((a==b) or (b==c) or (c==a)):
			print('Tipo de triangulo: isosceles')
		else:
			if ((a!=b) and (c!=a) and (b!=c)):
				print('Tipo de triangulo: escaleno')
			else:
				print('Tipo de triangulo: invalido')
	
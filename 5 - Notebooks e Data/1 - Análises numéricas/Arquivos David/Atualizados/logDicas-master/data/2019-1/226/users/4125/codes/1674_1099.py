# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("digite lado a: "))
b = float(input("digite lado b: "))
c = float(input("digite lado c: "))

print("Entradas: ",a, ", ",b, ", ",c)
x = "Tipo de triangulo: "
#condicoes para triangulo
if((a<0)or(b<0)or (c<0)or(a>= b + c)or (b>= c + a) or (c>=a+b)):
	print(x,"invalido")
else:
	if(a==b)and(b==c):
		print(x, "equilatero")
	else:
		if(a==b)or(b==c)or(c==a):
			print(x,"isosceles")
		else:
			print(x,"escaleno")	
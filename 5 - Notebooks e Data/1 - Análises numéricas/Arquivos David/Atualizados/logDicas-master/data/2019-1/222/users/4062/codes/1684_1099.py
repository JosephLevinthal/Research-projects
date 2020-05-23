# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a=float(input("valor de a: "))
b=float(input("valor de b: "))
c=float(input("valor de c: "))
tp=("Tipo de triangulo:")
print("Entradas:", a, ",", b, ",", c)
if(a<0)or(b<0)or(c<0)or(a>b+c)or(b>a+c)or(c>a+b):
	print(tp, "invalido")
else:
	if(a>0)and(b>0)and(c>0)and(a<b+c)and(b<a+c)and(c<a+b):
	elif(a==b)and(b==c):
		print(tp, "equilatero")
	elif(a==b)or(b==c)or(c==a):
		print(tp, "isosceles")
	elif(a!=b)or(b!=a)or(c!=a):
		print(tp,"escalendo")


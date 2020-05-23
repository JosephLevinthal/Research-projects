# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("valor de x: "))
a = float(input("valor de a: "))
b = float(input("valor de b: "))
if((b>a)or(x>=a)and(x<=b)):
	if((x>=a)and(x<=b)):
		print(x, "pertence ao intervalo", a, ",", b)
	elif((x!=a)and(x<a)or(x!=b)and(x>b)):
		print(x, "nao pertence ao intervalo", a, ",", b)
else:
	print("Entradas", a, "e", b, "invalidas")
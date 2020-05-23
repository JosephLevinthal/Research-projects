# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("insira um valor "))
a = float(input("insira um valor a "))
b = float(input("insira um valor b "))

if(b>a):
	if(a<=x and b<=b):
		print(x, "pertence ao intervalo", a,",", b)
	else:
		print(x, "nao pertence ao intervalo", a, ",", b)
else:
	print("Entradas", a,"e", b, "invalidas")
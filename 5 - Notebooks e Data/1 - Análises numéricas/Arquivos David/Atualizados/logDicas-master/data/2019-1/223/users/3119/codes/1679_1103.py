# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

x = float(input("Valor de x: "))
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))

if(b > a):
	if(a <= x and x <= b):
		print(x, "pertence ao intervalo", a,",",b)
	elif(a >= x or x >= b):
		print(x, "nao pertence ao intervalo",a,",",b)
else:
	print("Entradas",a,"e",b,"invalidas")
	
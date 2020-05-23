# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=float(input("Valor de x: "))
a=float(input("Valor de a: "))
b=float(input("Valor de b: "))
if (b <= a):
	print("Entradas", a,"e", b, "invalidas")
elif (x <= a or x >= b):
	print(x, "nao pertence ao intervalo", a, ",", b)
else:
	print(x, "pertence ao intervalo", a, ",", b)
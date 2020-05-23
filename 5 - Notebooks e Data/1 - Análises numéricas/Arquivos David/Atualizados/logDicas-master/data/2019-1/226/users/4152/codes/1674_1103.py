# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identifi Use as mensagens de erro para corrigir seu código.tinp
x = float(input("Digite aqui o valor de x: "))
a = float(input("Digite aqui o valor de a: "))
b = float(input("Digite aqui o valor de b: "))
if (b > a):
	if ((a <= x) and (x <= b)):
		 print(x, "pertence ao intervalo", a,",", b)
	else:
		 print(x, "nao pertence ao intervalo", a,",", b)
else:
		 print("Entradas", a, "e", b, "invalidas")
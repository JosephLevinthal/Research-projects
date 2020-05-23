# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

x = float(input("Digite o valor de x: "))
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

if(a <= x and x <= b):
	print(x,"pertence ao intervalo", a, ",", b)
elif(b <= a):
	print("Entradas", a, "e", b, "invalidas")
else:
	print(x, "nao pertence ao intervalo", a, ",", b)

	


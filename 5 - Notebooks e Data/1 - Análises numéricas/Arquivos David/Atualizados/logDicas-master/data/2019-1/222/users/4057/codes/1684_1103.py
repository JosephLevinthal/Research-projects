# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("Digite um numero: "))
a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))

if b >= a:
	if (a <= x and x <= b):
		print(x, "pertence ao intervalo ", a, ",", b)
	else :
		print(x, "nao pertence ao intervalo ", a, ",", b)
else: 
	print("Entradas ", a, "e ", b, "invalidas")

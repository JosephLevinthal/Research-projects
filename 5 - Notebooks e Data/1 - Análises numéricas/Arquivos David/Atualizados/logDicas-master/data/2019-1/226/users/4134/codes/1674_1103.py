# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("digite o numero x: "))
a = float(input("digite o numero a: "))
b = float(input("digite o numero b: "))

if (b >a):
	if (a<= x <= b):
		print( x, "pertence ao intervalo", a,",", b)
	elif ((x<a) or (x>b)):
		print(x, "nao pertence ao invervalo", a,",", b)
else:
	print("Entradas", a,"e",b,"invalidas")
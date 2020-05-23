# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("Numero real x: "))
a = float(input("Numero real a: "))
b = float(input("Numero real b: "))
if (b<=a):
	print("Entradas", a, "e", b, "invalidas")
elif ((a<=x) and (x<=b)):
	print(x, "pertence ao intervalo", a, ",", b)
else:	
	print(x, "nao pertence ao intervalo", a, ",", b)
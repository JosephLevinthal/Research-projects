# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=float(input("escolha um valor para x: "))
a=float(input("escolha um valor para a: "))
b=float(input("escolha um valor para b: "))
if (a<b) and (x<b) and (x>a):
	print(x, "pertence ao intervalo", a, ",", b)
elif (a<b) and (x>b):
	print(x, "nao pertence ao intervalo", a, ",", b)
elif (a<b) and (x<a):
	print(x, "nao pertence ao intervalo", a, ",", b)
else:
	print("Entradas", a, "e", b, "invalidas")
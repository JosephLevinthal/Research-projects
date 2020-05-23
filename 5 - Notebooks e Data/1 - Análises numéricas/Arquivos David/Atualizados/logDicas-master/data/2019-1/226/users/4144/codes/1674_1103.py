# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("digite um valor: "))
a = float(input("digite um valor: "))
b = float(input("digite um valor: "))
if((x>=a) and (x<=b)):
	print(x, "pertence ao intervalo", a,",", b)
elif(b<=a):
	print("Entradas", a, "e", b, "invalidas")
else:
	print(x, "nao pertence ao intervalo", a,",", b)
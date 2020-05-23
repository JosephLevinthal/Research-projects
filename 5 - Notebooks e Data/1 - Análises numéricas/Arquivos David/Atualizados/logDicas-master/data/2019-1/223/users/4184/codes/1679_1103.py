# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=float(input("valor de x: "))
a=float(input("valor de a: "))
b=float(input("valor de b: "))

if ((a<=x) and (b>=x)):
	print(x ,"pertence ao intervalo", a,",", b)
elif (b<=a):
	print("Entradas", a, "e", b, "invalidas")
elif ((a>=x) or (b<=x)):
	print(x ,"nao pertence ao intervalo", a,",", b)

# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("digite x: "))
a = float(input("digite a: "))
b = float(input("digite b: "))

if(b <= a):
	print("Entradas", a ,"e", b ,"invalidas")
else:
	if(a <= x and x <= b):
		print(x , "pertence ao intervalo", a,",", b)
	else:
		print(x ,"nao pertence ao intervalo", a,",", b)




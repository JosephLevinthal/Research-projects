# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("valor: "))                #Valor entre a,b
a = float(input("limite pela esquerda: ")) #Limite a
b = float(input("limite pela direita: "))  #Limite b

if b > a:
	if a <= x <= b:
		print(x, "pertence ao intervalo", a,",",b)
	else:
		print(x, "nao pertence ao intervalo", a,",",b)
else:
	print("Entradas",a ,"e", b, "invalidas")
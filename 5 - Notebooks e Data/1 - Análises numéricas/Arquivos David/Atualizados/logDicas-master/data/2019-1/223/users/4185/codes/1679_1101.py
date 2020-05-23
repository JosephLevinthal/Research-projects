# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

c= float(input("consumo: "))
ti= input("tipo: ")
preco=
if (c<=0) or (not ti=="R" or not ti=="I" or not ti=="C"):
	print("Entradas: ",c,"kwh e ",ti)
	print("Dados invalidos")
	
elif (ti=="R"):
	if (c>=500):
		preco = 0.44
	else:
		preco = 0.65
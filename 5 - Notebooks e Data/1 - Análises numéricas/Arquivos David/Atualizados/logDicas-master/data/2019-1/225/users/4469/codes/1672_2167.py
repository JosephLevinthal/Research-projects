# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = input()
y = input()

if(x.upper() == "BELEM"):
	if(y.upper() == "IDA"):
		print(350.0)
	else:
		print(650.0)
elif(x.upper() == "BORBA"):
	if(y.upper() == "IDA"):
		print(80.0)
	else:
		print(152.0)
elif(x.upper() == "COARI"):
	if(y.upper() == "IDA"):
		print(106.0)
	else:
		print(199.0)
elif(x.upper() == "HUMAITA"):
	if(y.upper() == "IDA"):
		print(200.0)
	else:
		print(390.0)
elif(x.upper() == "MANICORE"):
	if(y.upper() == "IDA"):
		print(150.0)
	else:
		print(280.0)
elif(x.upper() == "MAUES"):
	if(y.upper() == "IDA"):
		print(100.0)
	else:
		print(190.0)
else:
	print("Destino inexistente")
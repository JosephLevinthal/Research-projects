# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
destino = input("escreva a cidade de destino: ")
opcao = input("escreva o precurso? (ida/ida-e-volta): ")
if ((destino == "Belem") and (opcao == "ida")):
	valor = 350.0
	print (valor)
elif ((destino == "Belem") and (opcao == "ida-e-volta")):
	valor = 650.0
	print (valor)
elif ((destino == "Borba") and (opcao == "ida")):
	valor = 80.0
	print (valor)
elif ((destino == "Borba") and (opcao == "ida-e-volta")):
	valor = 152.0
	print (valor)
elif ((destino == "Coari") and (opcao == "ida")):
	valor = 106.0
	print (valor)
elif ((destino == "Coari") and (opcao == "ida-e-volta")):
	valor = 199.0
	print (valor)
elif ((destino == "Humaita") and (opcao == "ida")):
	valor = 200.0
	print (valor)
elif ((destino == "Humaita") and (opcao == "ida-e-volta")):
	valor = 390.0
	print (valor)
elif ((destino == "Manicore") and (opcao == "ida")):
	valor = 150.0
	print (valor)
elif ((destino == "Manicore") and (opcao == "ida-e-volta")):
	valor = 280.0
	print (valor)
elif ((destino == "Maues") and (opcao == "ida")):
	valor = 100.0
	print (valor)
elif ((destino == "Maues") and (opcao == "ida-e-volta")):
	valor = 190.0
	print (valor)
else:
	print ("Destino inexistente")
	
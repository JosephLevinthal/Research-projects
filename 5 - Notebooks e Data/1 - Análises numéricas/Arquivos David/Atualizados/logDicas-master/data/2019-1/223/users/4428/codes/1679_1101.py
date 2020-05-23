# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

consumo = float(input("Faixa de Consumo: "))
tipo = input("Tipo de Instalacao: ")


print("Entradas:", consumo,"kWh", "e tipo", tipo)

if(tipo == "R"):
	if(consumo < 0):
		print("Dados invalidos")
	elif(consumo <= 500):
		preco = consumo*0.44
	else:
		preco = consumo*0.65
elif(tipo == "I"):
	if(consumo < 0):
		preco = "Dados invalidos"
	elif(consumo <= 1000):
		preco = consumo*0.55
	else:
		preco = consumo*0.60
elif(tipo == "C"):
	if(consumo < 0):
		preco = "Dados invalidos"
	elif(consumo <=5000):
		preco = consumo*0.55
	else:
		preco = consumo*0.60

else:
		preco = "Dados invalidos"

print(preco)




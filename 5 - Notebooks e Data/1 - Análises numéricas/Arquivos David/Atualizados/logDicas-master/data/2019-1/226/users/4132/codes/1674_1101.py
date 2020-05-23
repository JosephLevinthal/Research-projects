# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
consumo = float(input("Digite o consumo:"))
tipo = input("Digite o tipo R OU I OU C: ").upper()

print("Entradas:",consumo,"kWh","e","tipo",tipo)

if(tipo=="R" and consumo>=0):
	if(consumo <=500.0):
		consumo = consumo*0.44
		print("Valor total: R$",round(consumo,2))
	else:
		consumo = consumo*0.65
		print("Valor total: R$",round(consumo,2))
elif(tipo == "C"and consumo>=0):
	if(consumo<=1000.0):
		consumo = consumo*0.55
		print("Valor total: R$",round(consumo,2))
	else:
		consumo = consumo*0.60
		print("Valor total: R$",round(consumo,2))
elif(tipo=="I"and consumo>=0):
	if(consumo<=5000.0):
		consumo=consumo*0.55
		print("Valor total: R$",round(consumo,2))
	else:
		consumo=consumo*0.60
		print("Valor total: R$",round(consumo,2))
else:
	print("Dados invalidos")

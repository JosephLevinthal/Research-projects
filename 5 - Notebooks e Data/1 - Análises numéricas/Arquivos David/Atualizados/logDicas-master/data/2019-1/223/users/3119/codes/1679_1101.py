# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

consumo = float(input("Digite o consumo de energia (em kWh): "))
tipo = input("Tipo de instalacao: ")
print("Entradas:", consumo,"kWh e tipo", tipo)
if((tipo == "R" or tipo == "I" or tipo == "C") and (consumo > 0)):
	if(tipo == "R" and consumo <= 500):
		print("Valor total: R$", round(consumo * 0.44, 2))
	elif(tipo == "R" and consumo > 500):
		print("Valor total: R$", round(consumo * 0.65,2))
	elif(tipo == "C" and consumo <= 1000):
		print("Valor total: R$", round (consumo * 0.55,2))
	elif(tipo == "C" and consumo > 1000):
		print("Valor total: R$", round(consumo * 0.60,2))
	elif(tipo == "I" and consumo <= 5000):
		print("Valor total: R$", round(consumo * 0.55,2))
	elif(tipo == "I" and consumo > 5000):
		print("Valor total: R$:", round(consumo * 0.60,))
else:
	print("Dados invalidos")
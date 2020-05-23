# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
total = float(input("digite valor: "))
tipo = input("digite tipo: ")

print("Entradas: " ,total, "kwh e tipo" ,tipo.upper())

if((tipo.upper() != "R" or tipo.upper() != "C" or  tipo.upper() != "I") and total < 0):
	print("Dados invalidos")
else:
	if(tipo.upper() == "R"):
		if(total <= 500):
			conta = total*0.44
		else:
			conta = total*0.65
	elif(tipo.upper() == "C"):
		if(total <= 1000):
			conta = total*0.55
		else:
			conta = total*0.60
	elif(tipo.upper() == "I"):
		if(total <= 5000):
			conta = total*0.55
		else:
			conta = total*0.60
	print("Valor total: ",round(conta, 2))
	

	
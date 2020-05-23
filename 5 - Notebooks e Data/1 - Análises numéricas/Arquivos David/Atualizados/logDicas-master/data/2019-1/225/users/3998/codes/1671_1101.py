# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
con = float(input("consumo de energia: "))
i = input("tipo de instalacao (R /I /C)")

print("Entradas: " + str(con) +" kWh e tipo " + i.upper())

if(con > 0 and i.upper() == "R" and con <= 500):
	print("Valor total: R$ " + str(round(con * 0.44, 2)))
	
elif(con > 0 and i.upper() == "R" and con > 500):
	print("Valor total: R$ " + str(round(con * 0.65, 2)))
	
elif(con > 0 and i.upper() == "C" and con <= 1000):
	print("Valor total: R$ " + str(round(con * 0.55, 2)))
	
elif(con > 0 and i.upper() == "C" and con > 1000):
	print("Valor total: R$ " + str(round(con * 0.60, 2)))
	
elif(con > 0 and i.upper() == "I" and con <= 5000):
	print("Valor total: R$ " + str(round(con * 0.55, 2)))
	
elif(con > 0 and i.upper() == "I" and con > 5000):
	print("Valor total: R$ " + str(round(con * 0.60, 2)))
	
else:
	print("Dados invalidos")

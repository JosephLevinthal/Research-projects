# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
consumo = float(input(""))
tipo = (input(""))
print("Entradas:", consumo, "kWh", "e", "tipo", tipo)
if(consumo >0):
   if ((consumo <= 500) and (tipo == "R")):
	   a = 0.44
	   b = (consumo*a)
	   print("Valor total: R$", round(b,2))
   elif ((consumo > 500) and (tipo == "R")):
	   a = 0.65
	   b = (consumo*a)
	   print("Valor total: R$", round(b,2))
   elif ((consumo <= 1000) and (tipo == "C")):
	   a = 0.55
	   b = (consumo*a)
	   print("Valor total: R$", round(b,2))
   elif ((consumo > 1000) and (tipo == "C")):
	   a = 0.60
	   b = (consumo*a)
	   print("Valor total: R$", round(b,2))
   elif ((consumo <= 5000) and (tipo == "I")):
	   a = 0.55
	   b = (consumo*a)
	   print("Valor total: R$", round(b,2))
   elif ((consumo > 5000) and (tipo == "I")):
	   a = 0.60
	   b = (consumo*a)
	   print("Valor total: R$", round(b,2))
else:
	print("Dados invalidos")

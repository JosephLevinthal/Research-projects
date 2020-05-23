# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c = float(input("consumo de energia:"))
t = input("tipo de instacao:")
print("Entradas:" , c , "kWh e tipo" , t)

if ((c < 0) or (t != "R") and (t != "C") and (t != "I")):
	print("Dados invalidos")
elif ((t == "R") and (c <= 500)):
	msg = c * 0.44
	print("Valor total: R$" , round(msg , 2))
elif((t == "R") and (c > 500)):
	msg = c * 0.65
	print("Valor total: R$" , round(msg , 2))
elif((t == "C") and (c <= 1000)):
	msg = c * 0.55
	print("Valor total: R$" , round(msg , 2))
elif ((t == "C") and (c > 1000)):
	msg =c * 0.60
	print("Valor total: R$" , round(msg , 2))
elif ((t == "I") and (c <= 5000)):
	msg = c * 0.55
	print("Valor total: R$" , round(msg , 2))
elif ((t == "I") and (c > 5000)):
	msg = c * 0.60
	print("Valor total: R$", round(msg , 2))
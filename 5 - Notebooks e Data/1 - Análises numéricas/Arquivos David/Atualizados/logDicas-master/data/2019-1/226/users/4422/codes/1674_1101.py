# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
con = float(input("Qual o consumo? "))
inst = input("Qual a instalacao? (r/i/c)")

print("Entradas: ",con, "kWh e tipo", inst.upper())

if(con<0 or inst.lower() != "r" and inst.lower() != "i" and inst.lower() != "c"):
	print("Dados invalidos")
	
else:
	if(inst.lower() == "r" and con<=500):
		c = con*0.44
		print("Valor total: ", "R$",round(c, 2))
	elif(inst.lower() == "r" and con>500):
		c = con*0.65
		print("Valor total: ", "R$",round(c, 2))
	elif(inst.lower() == "i" and con<=5000):
		c = con*0.55
		print("Valor total: ", "R$",round(c, 2))
	elif(inst.lower() == "i" and con>5000):
		c = con*0.60
		print("Valor total: ", "R$",round(c, 2))
	elif(inst.lower() == "c" and (con<=1000)):
		c = con*0.55
		print("Valor total: ", "R$",round(c, 2))
	elif(inst.lower() == "c" and con>1000):
		c = con*0.60
		print("Valor total: ", "R$",round(c, 2))
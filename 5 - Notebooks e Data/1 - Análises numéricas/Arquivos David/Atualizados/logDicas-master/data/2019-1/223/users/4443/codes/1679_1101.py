#Entrada do consumo de energia:
con=float(input("Qual o consumo de energia? "))
inst=input("Indique o tipo de instalacao: residencia (R), industria (I) ou comercio (C): ")
inst=inst.upper()

#Calculo do valor devido
if(con <= 0): 
	print("Entradas: ", con, " kWh e tipo", inst)
	print("Dados invalidos")
elif(inst != "R") and (inst != "I") and (inst != "C"):
	print("Entradas:", con,"kWh e tipo", inst)
	print("Dados invalidos")
elif(inst == "R") and (con <= 500):
	print("Entradas:", con,"kWh e tipo", inst)
	print("Valor total: R$", round(con*0.44, 2))
elif(inst == "R") and (con > 500):
	print("Entradas:", con,"kWh e tipo", inst)
	print("Valor total: R$", round(con*0.65, 2))	
elif(inst == "C") and (con <= 1000):
	print("Entradas:", con,"kWh e tipo", inst)
	print("Valor total: R$", round(con*0.55, 2))	
elif(inst == "C") and (con > 1000):
	print("Entradas:", con,"kWh e tipo", inst)
	print("Valor total: R$", round(con*0.60, 2))	
elif(inst == "I") and (con <= 5000):
	print("Entradas:", con,"kWh e tipo", inst)
	print("Valor total: R$", round(con*0.55, 2))	
elif(inst == "I") and (con > 5000):
	print("Entradas:", con,"kWh e tipo", inst)
	print("Valor total: R$", round(con*0.60, 2))	
	
			 
con = float(input("consumo de energia:"))
tipo = input("tipo de instalacao: (R/I/C)")

if(con < 0):
	print("Entradas:",con,"kWh e tipo",tipo)
	print("Dados invalidos")
	
elif(tipo == "R" and con <= 500):
	preco = 0.44
	total = con * preco
	print("Entradas:",con,"kWh e tipo",tipo)
	print("Valor total: R$",round(total,2))
elif(tipo == "R" and con > 500):
	preco = 0.65
	total = con * preco
	print("Entradas:",con,"kWh e tipo",tipo)
	print("Valor total: R$",round(total,2))
elif(tipo == "I" and con <= 5000):
	preco = 0.55
	total = con * preco
	print("Entradas:",con,"kWh e tipo",tipo)
	print("Valor total: R$",round(total,2))
elif(tipo == "I" and con > 5000):
	preco = 0.60
	total = con * preco
	print("Entradas:",con,"kWh e tipo",tipo)
	print("Valor total: R$",round(total,2))
elif(tipo == "C" and con <= 1000):
	preco = 0.55
	total = con * preco
	print("Entradas:",con,"kwh e tipo",tipo)
	print("Valor total: R$",round(total,2))
elif(tipo == "C" and con > 1000):
	preco = 0.60
	total = con * preco
	print("Entradas:",con,"kwh e tipo",tipo)
	print("Valor total: R$",round(total,2))
else:
	print("Entradas:",con,"kwh e tipo",tipo)
	print("Dados invalidos")

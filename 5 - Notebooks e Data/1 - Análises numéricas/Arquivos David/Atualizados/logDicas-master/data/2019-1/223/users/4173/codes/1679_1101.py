a = float(input("Consumo:"))
b = input("Residencia:").upper()

if ((a > 0) and (a <= 500) and (b == "R")):
	d = a*0.44 
	n = round(d,2)
	print("Entradas:", a ,"kWh e tipo", b)
	print("Valor total: R$" ,n)
elif ((a > 500) and (b == "R")):
	d = a*0.65
	n = round(d,2)
	print("Entradas:", a ,"kWh e tipo", b)
	print("Valor total: R$" ,n)
elif ((a > 0) and (a <= 1000) and (b == "C")):
	d = a*0.55
	n = round(d,2)
	print("Entradas:", a ,"kWh e tipo", b)
	print("Valor total: R$" ,n)
elif ((a > 1000) and (b == "C")):
	d = a*0.60
	n = round(d,2)
	print("Entradas:", a ,"kWh e tipo", b)
	print("Valor total: R$" ,n)
elif ((a > 0) and (a <= 5000) and (b == "I")):
	d = a*0.55
	n = round(d,2)
	print("Entradas:", a ,"kWh e tipo", b)
	print("Valor total: R$" ,n)
elif ((a > 5000) and (b == "I")):
	d = a*0.60
	n = round(d,2)
	print("Entradas:", a ,"kWh e tipo", b)
	print("Valor total: R$" ,n)
else:
	k = "Dados invalidos"
	print("Entradas:", a ,"kWh e tipo", b)
	print(k)

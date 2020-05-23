cons = float(input("Consumo de energia em kWh: "))
ins = input("Tipo de instalacao: ").upper()

print("Entradas:",cons,"kWh e tipo", ins)

if((ins != "R" and ins != "I" and ins !="C") or (cons < 0)):
	print("Dados invalidos")
elif(ins == "R"):
	if(cons <= 500):
		x = cons*0.44
		print("Valor total: R$",round(x, 2))
	else:
		x = cons*0.65
		print("Valor total: R$",round(x, 2))
elif(ins=="C"):
	if(cons<=1000):
		x = cons*0.55
		print("Valor total: R$",round(x, 2))
	else:
		x =(cons*0.60)
		print("Valor total: R$",round(x, 2))
elif(ins=="I"):
	if(cons<=5000):
		x = cons*0.55
		print("Valor total: R$",round(x, 2))
	else:
		x = cons*0.6
		print("Valor total: R$",round(x, 2))


	
	
		




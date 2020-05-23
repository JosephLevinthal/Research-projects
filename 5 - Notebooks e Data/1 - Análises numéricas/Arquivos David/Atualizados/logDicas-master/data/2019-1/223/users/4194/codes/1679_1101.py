cons = float(input("Consumo em kWh: "))
ti = input("Tipo de instalacao: R/C/I ").upper()
print("Entradas:", cons, "kWh e tipo", ti)
r1 = round(cons * 0.44, 2)
r2 = round(cons * 0.65, 2)
c1 = round(cons * 0.55, 2)
c2 = round(cons * 0.60, 2)
i1 = round(cons * 0.55, 2)
i2 = round(cons * 0.60, 2)

if((ti=="R" or ti=="C" or ti=="I") and cons>0):
	if(cons <=500 and ti == "R"):
		print("Valor total: R$", r1)
	elif(cons >500 and ti == "R"):
		print("Valor total: R$", r2)
	elif(cons <=1000 and ti == "C"):
		print("Valor total: R$", c1)
	elif(cons >1000 and ti == "C"):
		print("Valor total: R$", c2)
	elif(cons <=5000 and ti == "I"):
		print("Valor total: R$", i1)
	elif(cons >5000 and ti == "I"):
		print("Valor total: R$", i2)
else:
	print("Dados invalidos")
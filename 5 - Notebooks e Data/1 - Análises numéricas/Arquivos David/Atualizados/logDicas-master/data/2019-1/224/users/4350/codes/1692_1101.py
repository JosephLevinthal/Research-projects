b = float(input("consumo"))
a = input("tipo de instalacao")
print("Entradas:", b, "kWh e tipo", a)
if(a=="R"):
	if(b<0):
		print("Dados invalidos")
	elif(b<=500):
		c = round(b*0.44, 2)
	else:
		c = round(b*0.65, 2)
elif(a=="I"):
	if(b<0):
		print("Dados invalidos")
	elif(b<=1000):
		c = round(b*0.55, 2)
	else:
		c = round(b*0.60, 2)
elif(a=="C"):
	if(b<0):
		print("Dados invalidos")
	elif(b<=5000):
		c = round(b*0.55, 2)
	else:
		c = round(b*0.60, 2)
else:
	print("Dados invalidos")
print("Valor total: R$", c)	
		
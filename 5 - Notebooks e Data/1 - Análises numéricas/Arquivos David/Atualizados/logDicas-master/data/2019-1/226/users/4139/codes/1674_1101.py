ce = float(input("digite o consumo de energia:"))
t = input("tipo de instalacao[R,I ou C]:").upper()
y = "Valor total: R$ "

print("Entradas: ",ce," kWh e tipo ",t)

if(ce<0):
	print("Dados invalidos")
elif(t=="R"):
	if(ce<=500):
		print(y,round(ce*0.44,2))
	else:
		print(y,round(ce*0.65,2))
elif(t=="C"):
	if(ce<=1000):
		print(y,round(ce*0.55,2))
	else:
		print(y,round(ce*0.60,2))
elif(t=="I"):
	if(ce<=5000):
		print(y,round(ce*0.55,2))
	else:
		print(y,round(ce*0.60,2))
else:
	print("Dados invalidos")
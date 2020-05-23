c = float(input("Digite o consumo: "))
t = input("Digite a instalacao: ").upper()
print("Entradas:",c , "kwh", "e", "tipo", t)

if(t=="R" and c >=0):
	if(c <=500.0):
		consumo= c *0.44
		print("Valor total: R$", round(consumo, 2))
	else:
		consumo= c *0.65
		print("valor total: R$", round(consumo, 2))
elif(t=="I" and c>=0):
	if(c<=5000):
		consumo= c*0.55
		print("valor tota: R$", round(consumo, 2))
	else:
		consumo = c*0.60
		print("valor total: R$", round(consumo, 2))
elif(t=="C" and c>=0):
	if(c<=1000):
		consumo= c*0.55
		print("valor total: R$", round(consumo, 2))
	else:
		print("Dados invalidos")
	
#Preço 
pr= float(input("Insira o preco:"))
pa= float(input("Insira o total pago:"))
pf1=(pa-pr)
pf2=(pr-pa)

if (pr<=pa):
	print("Troco de", round(pf1,2))
else:
	print("Falta", round(pf2,2))


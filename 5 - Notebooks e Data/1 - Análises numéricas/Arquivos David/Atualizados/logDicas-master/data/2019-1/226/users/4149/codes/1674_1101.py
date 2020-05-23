a = float(input("consumo de energia: "))
b = input("tipo de instalacao: ").upper()

print("Entradas:", a, "kWh", "e", "tipo", b)

if(b=="R" and a>=0):
	if(a<=500):
		print("Valor total: R$", round((0.44*a),2))
	else:
		print("Valor total: R$", round((0.65*a),2))
elif(b=="C" and a>=0):
	if(a<=1000):
		print("Valor total: R$", round((0.55*a),2))
	else:
		print("Valor total: R$", round((0.60*a),2))
       
elif(b=="C") and (a>=0):
	if(a<=5000):
		print("Valor total: R$", round((0.55*a),2))
	else:
		print("Valor total: R$", round((0.60*a),2))

else:
    print("Dados invalidos")
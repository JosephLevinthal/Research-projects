juros = float(input("juros ao mes: "))
ap = float(input("valor: "))
total = 1500*(1+juros)**36
if(total>=ap):
		print(round(total, 2))
		print("Sim")
else:
		print(round(total, 2))
		print("Nao")
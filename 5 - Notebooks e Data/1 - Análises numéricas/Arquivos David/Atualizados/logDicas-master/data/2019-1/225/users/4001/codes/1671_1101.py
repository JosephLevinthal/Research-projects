# Entradas
E = float(input("Consumo de energia: "))
T = input("Tipo de instalacao: (R/I/C)? ")
print("Entradas: ", E, " kWh e tipo ", T)
# Condicoes
if (T != "R") and (T != "I") and (T != "C") or (E < 0):
	print("Dados invalidos")
elif (T == "R") and (E <= 500) :
	Z = E * 0.44
	print("Valor total: R$ ", round(Z, 2))
elif (T == "R") and (E > 500):
	Z = E * 0.65
	print("Valor total: R$ ", round(Z, 2))
elif (T == "C") and (E <= 1000):
	Z = E * 0.55
	print("Valor total: R$ ", round(Z, 2))
elif (T == "C") and (E > 1000):
	Z = E * 0.60
	print("Valor total: R$ ", round(Z, 2))
elif (T == "I") and (E <= 5000):
	Z = E * 0.55
	print("Valor total: R$ ", round(Z, 2))
elif (T == "I") and (E > 5000):
	Z = E * 0.60
	print("Valor total: R$ ", round(Z, 2))
	



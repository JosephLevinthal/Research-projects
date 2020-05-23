quantidadedevotos1 = int(input(" "))
quantidadedevotos2 = int(input(" "))
votosvalidos = quantidadedevotos1 + quantidadedevotos2 
if (quantidadedevotos > votosvalidos):
	print("Ambrosio Rutra")
else:
	print("Demelza Olecram")
porcent = (quantidadedevotos1/votosvalidos) * (100)
print(round(porcent, 2))

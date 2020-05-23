I = int(input("Idade: "))
IMC = float(input("IMC: "))
print("Entradas: ", I," anos e IMC ", IMC)
# Condicoes
if (I <= 0) or (I > 130) or (IMC <= 0):
	print("Dados invalidos")
elif (I < 45) and (IMC < 22):
	print("Risco: Baixo ")
elif ( I < 45) and (IMC >= 22):
	print("Risco: Medio")
elif (I >= 45) and (IMC < 22):
	print("Risco: Medio")
elif (I >= 45) and (IMC >= 22):
	print("Risco: Alto")
	
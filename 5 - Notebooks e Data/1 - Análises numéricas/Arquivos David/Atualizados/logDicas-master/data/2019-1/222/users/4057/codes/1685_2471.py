i = int(input("Idade: "))
m = float(input("Massa corporal: "))

print ("Entradas: ", i, "anos e IMC ", m)
if (i > 0) and (i <= 130)and (m > 0):
	if (i < 45) and (m < 22):
		print("Risco: Baixo")
	elif (i < 45) and (m >= 22):
		print("Risco: Medio")
	elif (i >= 45) and (m < 22):
		print("Risco: Medio")
	elif (i >= 45) and (m >= 22):
		print("Risco: Alto")
else:
	print("Dados invalidos")
i = int(input("Digite aqui a idade: "))
m = float(input("Digite aquio indece de massa corporal: "))

if (((i <= 0) or (i > 130)) or (m <= 0)):
	print("Entradas:", i, "anos e IMC", m)
	print("Dados invalidos")
else:
	if ((i > 45) and (m < 22.0)):
		print("Entradas:", i, "anos e IMC", m)
		print("Risco:", "Baixo")
	elif (i > 45) or (i >= 45) and (m >= 22.0):
		print("Entradas:", i, "anos e IMC", m)
		print("Risco:", "Medio")
	elif (i >= 45) and (m >= 22.0):
		print("Entradas:", i, "anos e IMC", m)
		print("Risco:", "Alto")
	
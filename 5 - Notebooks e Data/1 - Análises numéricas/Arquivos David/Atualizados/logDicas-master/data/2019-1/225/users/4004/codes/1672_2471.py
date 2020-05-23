age = int(input("idade: "))
imc = float(input("IMC: "))

print("Entradas:",age,"anos e IMC",imc)

if age > 130 or age < 0 or (imc <= 0):
	print("Dados invalidos")
else:
	if age < 45:
		if imc < 22.0:
			Z = "Baixo"
		else:
			Z = "Medio"
	else:
		if imc < 22.0:
			Z = "Medio"
		else:
			Z = "Alto"
	print("Risco:",Z)
i = int(input("idade:"))
imc = float(input("digite IMC:"))

print("Entradas:",i,"anos e IMC",imc)

if(i > 0)and(imc > 0):
	if(imc<22.0):
		if(i<45):
			print("Risco: Baixo")
		elif(i>=45):
			print("Risco: Medio")
	elif(imc>=22.0):
		if(i<45):
			print("Risco: Medio")
		elif(i>=45):
			print("Risco: Alto")

else:
	print("Dados invalidos")

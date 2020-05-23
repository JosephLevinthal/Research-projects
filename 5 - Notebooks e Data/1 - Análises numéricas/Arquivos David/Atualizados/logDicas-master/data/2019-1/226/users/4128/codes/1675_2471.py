i = int(input("idade:"))
imc = float(input("massa corporal:"))

print("Entradas: ",i, "anos e IMC",imc)

if((imc <= 0) or (i <= 0 ) or (i >= 130)):
	print("Dados invalidos")
elif((i < 45) and (imc < 22)):
	print("Risco: Baixo")
elif((i < 45) and (imc >= 22)):
	print("Risco: Medio")
elif((i >= 45) and (imc < 22)):
	print("Risco: Medio")
elif((i >= 45) and (imc >= 22)):
	print("Risco: Alto")





age=int(input("entre com a sua idade: "))
imc=float(input("entre com o seu imc: "))
print("entradas:",age,"anos e IMC",imc)


if(age>0)and(age<130)and(imc>0):
	if(imc<22)and(age<45):
		print("Risco: Baixo")
	elif(imc<22)and(age>=45):
		print("Risco: Medio")
	elif(imc>=22)and(age<45):
		print("Risco: Medio")
	elif(imc>=22)and(age>=45):
		print("Risco: Alto")
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")
	
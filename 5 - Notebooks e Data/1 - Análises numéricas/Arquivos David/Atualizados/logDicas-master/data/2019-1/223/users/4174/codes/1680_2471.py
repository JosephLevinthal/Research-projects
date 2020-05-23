idade = int(input("qual a idade:"))
imc =float(input("qual o imc:"))

if(idade < 45):
	if(imc<22):
		print("Entradas:",idade, "anos e IMC",imc)
		print("Risco: Baixo")
	else:
		print("Entradas:",idade, "anos e IMC",imc)
		print("Risco: Medio")
elif(idade >= 45):
	if(imc < 22):
		print("Entradas:",idade, "anos e IMC",imc)
		print("Risco: Medio")
	else:
		print("Entradas:",idade, "anos e IMC",imc)
		print("Risco: Alto")
else:
	print('Dados invalidos')
	
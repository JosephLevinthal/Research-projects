idade = int(input("idade: "))
indice = float(input("IMC: "))
if(idade > 0 and indice > 0):
	if(indice < 22 and idade < 45):
		print("Entradas:",idade,"anos e IMC",indice)
		print("Risco: Baixo")
	elif(indice < 22 and idade >= 45):
		print("Entradas:",idade,"anos e IMC",indice)
		print("Risco: Medio")
	elif(indice >= 22 and idade >= 45):
		print("Entradas:",idade,"anos e IMC",indice)
		print("Risco: Alto")
	elif(indice >= 22 and idade < 45):
		print("Entradas:",idade,"anos e IMC",indice)
		print("Risco: Medio")
	else:
		print("Entradas:",idade,"anos e IMC",indice)
		print("Dados invalidos")
else:
	print("Entradas:",idade,"anos e IMC",indice)
	print("Dados invalidos")

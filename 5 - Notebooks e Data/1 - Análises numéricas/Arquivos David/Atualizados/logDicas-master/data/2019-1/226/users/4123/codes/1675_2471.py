i = int(input())
imc = float(input())
if i<=0 or i>130 or imc<=0:
	print("Entradas:",i ,"anos e IMC" , imc)
	print("Dados invalidos")
else:
	print("Entradas:",i ,"anos e IMC" , imc)
	if (i<45 and imc<22):
		print("Risco: Baixo")
	elif(i>=45 and imc >=22):
		print("Risco: Alto")
	else:
		print("Risco: Medio")
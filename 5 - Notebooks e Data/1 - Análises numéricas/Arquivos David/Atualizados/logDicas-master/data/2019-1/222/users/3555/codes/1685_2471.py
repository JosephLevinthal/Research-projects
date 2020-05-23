idade = int(input())
imc = float(input())
if(0 <= idade < 130 and 0 < imc):
	print("Entradas:",idade,"e IMC",imc)
	
	if(idade <45):
		if(imc < 22.0):
			print("Risco: Baixo")
		elif(imc >=22.0):
			print("Risco: Medio")
	elif(idade >= 45):
		if(imc < 22.0):
			print("Risco: Medio")
		elif(imc >=22.0):
			print("Risco: Alto")
elif(0 > idade or idade > 130 or 0 >= imc):
	print("Entradas:",idade,"e IMC",imc)
	print("Dados Invalidos")
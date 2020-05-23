i=int(input("Digite a idade: "))
imc=float(input("Digite o imc: "))
print("Entradas:",i,"anos e IMC",imc)
if(i<=0 or i>130 or imc<=0):
	mensagem= "Dados invalidos"
	print(mensagem)
else:
	if(i<45 and imc<22):
		mensagem="Baixo"
		print("Risco:", mensagem)
	elif(i<45 and imc>=22):
		mensagem="Medio"
		print("Risco:", mensagem)
	elif(i>=45 and imc<22):
		mensagem="Medio"
		print("Risco:", mensagem)
	elif(i>=45 and imc>=22):
		mensagem="Alto"
		print("Risco:", mensagem)
	
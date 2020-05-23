idade = int(input("Digite a idade: "))
imc = float(input("Digite o imc: "))
print("Entradas: ", idade, "anos e IMC ", imc)
if(idade <= 0 or idade > 130 or imc <= 0):
	print("Dados invalidos")
elif(idade < 45):
	if(imc < 22):
		print("Risco: Baixo")
	else: 
		print("Risco: Medio")
elif(idade >= 45):
	if(imc < 22):
		print("Risco: Medio")
	else: 
		print("Risco: Alto")
	
	
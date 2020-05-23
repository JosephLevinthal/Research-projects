idade = int(input("informe a idade: "))
imc = float(input("indice de massa corporal: "))
if(idade <= 0 or idade > 130 or imc <= 0):
	print("Entradas: " ,idade,"anos e IMC" ,imc)
	print("Dados invalidos")
elif(imc < 22 and idade < 45):
	print("Entradas: " ,idade,"anos e IMC" ,imc)
	print("Risco: Baixo")
elif(imc >= 22 and idade < 45):
	print("Entradas: " ,idade,"anos e IMC" ,imc)
	print("Risco: Medio")
elif(imc < 22 and idade >= 45):
	print("Entradas: " ,idade,"anos e IMC" ,imc)
	print("Risco: Medio")
elif(imc >= 22 and idade >= 45):
	print("Entradas: " ,idade,"anos e IMC" ,imc)
	print("Risco: Alto")
	
	




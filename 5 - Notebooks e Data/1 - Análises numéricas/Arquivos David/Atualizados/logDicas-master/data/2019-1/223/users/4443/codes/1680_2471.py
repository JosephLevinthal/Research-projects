#Entrada da idade e indice de massa corporea:
y = int(input("Digite a sua idade: "))
imc = float(input("Digite o seu IMC: "))

if(y <= 0) or (y >= 130) or (imc <= 0):
	print("Entradas:", y, "anos e IMC", imc)
	print("Dados invalidos")
elif(y < 45) and (imc < 22.0):	
	print("Entradas:", y, "anos e IMC", imc)
	print("Risco: Baixo")
elif(y < 45) and (imc >= 22.0):
	print("Entradas:", y, "anos e IMC", imc)
	print("Risco: Medio")
elif(y >= 45) and (imc <= 22.0):
	print("Entradas:", y, "anos e IMC", imc)
	print("Risco: Medio")
elif(y >= 45) and (imc >= 22.0):
	print("Entradas:", y, "anos e IMC", imc)
	print("Risco: Alto")
	

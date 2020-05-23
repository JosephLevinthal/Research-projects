ida=int(input("Insira a idade:"))
imc= float(input("Insira o IMC:"))
print("Entradas:",ida,"anos e IMC",imc)
if(ida>130 or ida<=0 or imc<=0):
	print("Dados invalidos")

elif(ida<45 and imc<22):
	print("Risco: Baixo")
elif(ida>45 and imc<=22):
	print("Risco: Medio")
elif(ida>=45 or imc<22):
	print("Risco: Medio")
elif(ida>=45 and imc>=22):
	print("Risco: Alto")
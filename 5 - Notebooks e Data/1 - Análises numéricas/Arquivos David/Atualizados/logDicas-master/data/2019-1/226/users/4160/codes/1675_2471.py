i = int(input("Idade: "))
IMC = float(input("IMC: "))

print("Entradas:",i, "anos e IMC",IMC)

if ((i<=0 or i>130) or (IMC <=0)):
	print("Entradas:",i, "anos e IMC",IMC)
	print("Dados invalidos")
elif(i<45 and IMC < 22):
	print("Risco: Baixo")
elif(i>=45 and IMC< 22):
	print("Risco: Medio")
elif(i<45 and IMC>=22):
	print("Risco: Medio")	
elif(i>=45 and IMC>=22):
	print("Risco: Alto")
		
		
		
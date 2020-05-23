i=int(input("Digite a idade: "))
m=float(input("Digite o IMC: "))

print("Entradas:",i,"anos e IMC",m)
if(i<=0 or i>130 or m<=0):
	print("Dados invalidos")
elif(i<45 and m<22.0):
	print("Risco: Baixo")
elif(i<45 and m>=22.0):
	print("Risco: Medio")
elif(i>=45 and m<22.0):
	print("Risco: Medio")
elif(i>=45 and m>=22.0):
	print("Risco: Alto")
	
	
ida=int(input("idade:"))
imc=float(input("imc:"))

print("Entradas: {} anos e IMC {}".format(ida,imc))

if ((ida<=0 or ida>130) and imc<=0):
	print("Dados invalidos")
elif(ida<45 and imc<22):
	print("Risco: Baixo")
elif(ida>=45 and imc<22):
	print("Risco: Medio")
elif(ida<45 and imc>=22):
	print("Risco: Medio")
elif(ida>=45 and imc>=22):
	print("Risco: Alto")
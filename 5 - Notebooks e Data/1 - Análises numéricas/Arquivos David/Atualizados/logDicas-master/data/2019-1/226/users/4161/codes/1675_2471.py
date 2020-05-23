idade = int(input("idade: "))
imc = float(input("IMC: "))
print("Entradas:", idade, "anos e IMC",imc)

if (idade<=0) or (idade>=130) or (imc<=0):
	print("Dados invalidos")
elif (idade<45) and (imc<22.0):
	print("Risco: Baixo")
elif (idade>=45) and (imc<22.0):
	print("Risco: Medio")
elif (idade<45) and (imc>=22.0):
	print("Risco: Medio")
elif (idade>=45) and (imc>=22.0):
	print("Risco: Alto")

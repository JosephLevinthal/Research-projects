idade = int(input("Idade: "))
imc = float(input("IMC: "))

print ("Entradas:",idade,"anos e IMC",imc)

if (idade <= 0) and (idade > 130) and (imc <= 0):
	risco = "Dados invalidos"
	print (risco)
	
elif idade < 45 and imc < 22:
	risco = "Baixo"
	print ("Risco:",risco)
	
elif idade < 45 and imc >= 22:
	risco = "Medio"
	print ("Risco:",risco)

elif idade >= 45 and imc < 22:
	risco = "Medio"
	print ("Risco:",risco)
		
elif idade >= 45 and imc >= 22:
	risco = "Alto"
	print ("Risco:",risco)

else:
	risco = "Dados invalidos"
	print (risco)
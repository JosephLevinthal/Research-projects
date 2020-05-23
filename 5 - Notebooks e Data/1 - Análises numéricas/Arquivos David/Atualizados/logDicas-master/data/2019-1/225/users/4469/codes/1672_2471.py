idade = int(input())
imc = float(input())

print("Entradas: " + str(idade) + " anos e IMC " + str(imc))

if((idade <= 0) or (idade > 130) or (imc <= 0.0)):
	print("Dados invalidos")
else:
	if((idade < 45) and (imc < 22.0)):
		print("Risco: Baixo")
	elif(((idade < 45) and (imc >= 22.0)) or ((idade >= 45) and (imc < 22.0))):
		print("Risco: Medio")
	else:
		print("Risco: Alto")
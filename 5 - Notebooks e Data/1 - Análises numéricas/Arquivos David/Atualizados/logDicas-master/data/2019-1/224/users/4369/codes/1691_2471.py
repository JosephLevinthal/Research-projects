idade = int(input("Digite sua idade: "))
imc = float(input("Digite o seu imc: "))

if idade <= 0 or idade > 130 or imc <= 0:
	print("Entradas:",idade, "anos", "e", "IMC", imc)
	print("Dados invalidos")
elif idade < 45 and imc < 22.0:
	print("Entradas:",idade, "anos", "e", "IMC", imc)
	print("Risco:", "Baixo")
elif idade < 45 and imc >= 22.0:
	print("Entradas:",idade, "anos", "e", "IMC", imc)
	print("Risco:", "Medio")
elif idade >= 45 and imc < 22.0:
	print("Entradas:",idade, "anos", "e", "IMC", imc)
	print("Risco:", "Medio")
elif idade >= 45 and imc >= 22:
	print("Entradas:",idade, "anos", "e", "IMC", imc)
	print("Risco:", "Alto")
	
	
	
	
	
	
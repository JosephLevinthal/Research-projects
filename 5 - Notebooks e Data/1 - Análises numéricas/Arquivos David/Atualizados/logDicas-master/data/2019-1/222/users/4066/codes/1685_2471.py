idade = int(input("Idade: "))
imc = float(input("IMC: "))

print("Entradas: {} anos e IMC {}".format(idade, imc)

if ((idade <= 0) or (idade > 130) or (imc <= 0)):
print("Dados invalidos")
elif (idade < 45):
	if (imc < 22):
		risco = "Baixo"
	if (imc >= 22):
		risco = "Medio"
elif (idade >= 45):
	if (imc < 22)
		risco = "Medio"
	if (imc >= 22)
		risco = "Alto"

print("Risco: {}".format(risco))
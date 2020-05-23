idade = int(input("digite idade: "))
IMC = float(input("digite IMC: "))

print("Entradas: " ,idade, "anos e IMC" ,IMC,)

if(idade <= 0 or idade > 130 or IMC <= 0):
	print("Dados invalidos")
else:
	if(idade < 45 and IMC < 22.0):
		print("Risco: Baixo")
	elif(idade < 45 and IMC >= 22.0):
		print("Risco: Medio")
	elif(idade >= 45 and IMC < 22.0):
		print("Risco: Medio")
	elif(idade >= 45 and IMC >= 22.0):
		print("Risco: Alto")



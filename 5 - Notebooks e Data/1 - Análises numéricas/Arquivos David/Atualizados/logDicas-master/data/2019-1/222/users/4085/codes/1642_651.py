altura = float(input("escreva a altura da pessoa: "))
opcao = input("escreva o sexo da pessoa? (M/F): ")
if (opcao == "M"):
	pesoideal = (72.7 * altura) - 58
else:
		pesoideal = (62.1 * altura) - 44.7
print(round(pesoideal, 2))
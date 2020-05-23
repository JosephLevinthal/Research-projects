escolha = input("L/S")
quant1 = float(input("quantos L/S? "))
quant2 = float(input("quantos refeicoes? "))
conta1 = (quant1 * 5) + (quant2 * 4)
contas = (quant1 * 3.50) + (quant2 * 4)

if (escolha == "L"):
	print(round(conta1, 2))
else:
	print(round(contas, 2))

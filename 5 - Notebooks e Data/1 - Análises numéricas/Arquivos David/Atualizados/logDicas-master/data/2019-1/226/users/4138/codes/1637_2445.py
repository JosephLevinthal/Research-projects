opcao = input("escolha a conversao: (C/F)")
T = float(input("valor da temperatura : "))


C1 = ((5 * T) - 160)/9

F1 = ((9 * T) + 160)/5

if (opcao.upper() == "F"):
		mensagem = C1
		print(round(C1,2))
else:
	mensagem = F1
	print(round(F1,2))
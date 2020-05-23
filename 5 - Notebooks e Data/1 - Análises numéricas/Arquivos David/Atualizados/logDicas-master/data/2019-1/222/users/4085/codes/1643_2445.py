opcao = input("em qual escala esta representada? (C/F): ")
valor = float(input("escreva o valor da temperatura: "))
if (opcao == "C"):
	temperatura = (9 * valor + 160)/5
else:
	temperatura = (5 * valor - 160) / 9
print(round(temperatura, 2))
mensagem = input("Digite o resultado: ")

vitoria = 0
empate = 0
add1 = 0
add2 = 0

if (mensagem.upper() == "V"):
	add1 = 3
	vitoria = -3
elif (mensagem.upper() == "E"):
	add2 = 1
	empate = -1

while(mensagem.upper() != "X"):
	if (mensagem.upper() == "V"):
		vitoria = vitoria + 3
	elif(mensagem.upper() == "E"):
		empate = empate + 1
	mensagem = str(input("Digite o resultado: "))

print("Total de pontos das vitorias: ", vitoria+add1)
print("Total de pontos dos empates: ", empate+add2)
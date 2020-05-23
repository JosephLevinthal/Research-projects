P1 = int(input("digite a primeira posicao:"))
posicao = 0
pontos1 = 0
while(P1 > 0 and P1 and P1 != 0):
	if(P1 == 1):
		pontos2 = 20
	elif(P1 == 2):
		pontos2 = 15
	elif(P1 == 3):
		pontos2 = 10
	elif(P1 < 0):
		pontos = 0
	elif(P1 > 10):
		pontos = 0
	elif(P1 > 3 and P1 < 11):
		pontos2 = 11 - P1
	total = pontos1 + pontos2
	pontos1 = total
	P1 = int(input("digite as outras colocacoes:"))
print(total)
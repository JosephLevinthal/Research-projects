k = int(input("qual a posicao do jogador: "))
pontos = 0
soma = 0
while(k != 0):
	if(k == 1):
		soma = soma + 20
		pontos = pontos + 1
	elif(k == 2):
			soma = soma + 15
			pontos = pontos + 1
	elif(k == 3):
		soma = soma + 10
		pontos = pontos + 1
	elif(k>=4 and k<=11):
		soma = soma + (11-k)
		pontos = pontos + 1
	k = int(input("qual a posicao do jogador: "))		
print(soma)
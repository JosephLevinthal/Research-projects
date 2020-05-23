posicao = int(input("posicao: "))
#primeiro = 20
#segundo = 10
#demais = 11 - posicao
pontuacao = 0
while(posicao != 0):
	if(posicao==1):
		pontos = (20)
	elif(posicao == 2):
		pontos = 15
	elif(posicao == 3):
		pontos = 10
	elif(posicao >=4 and posicao <=10):
		pontos = 11 - posicao
	else:
		pontos = 0
	posicao = (int(input("posicao: ")))
	pontuacao = pontuacao + pontos
print(pontuacao)

from numpy import *
e = array(eval(input("Digite as jogadas de Eusapia: ")))
b = array(eval(input("Digite a jogadas de Barsanulfo: ")))
i = 0 # contador da posicao do vetor
es = 0 #vitorias de Eusapia
br = 0 #vitorias de Barsanulfo

while(i < len(e)): #percorre todas as posicoes do vetor de 0 a n
	if(e[i] == 11 and b[i] == 33) or (e[i] == 22 and b[i] == 11) or (e[i] == 33 and b[i] == 22): #situacoes que ela vece
		es = es+1 #incremento no numero de vitorias dela
	elif(b[i] == 11 and e[i] == 33) or (b[i] == 22 and e[i] == 11) or (b[i] == 33 and e[i] == 22): #situacoes que ele vence
		br = br+1 #incrementa no numero de vitorias dele
	i = i +1 #incremento da variavel contadora
print(len(e)) #imprime o tamanho do vetor
if(es>br): #comparacao do numero de vitorias de es
	print("EUSAPIA") #imprime se ela tiver mais vitorias que ele
elif(br>es): #comparacao do numero de vitorias de br
	print("BARSANULFO") #imprime se ele tiver mais vitorias que ela
else:
	print("EMPATE") #imprime se o numero de vitorias fo

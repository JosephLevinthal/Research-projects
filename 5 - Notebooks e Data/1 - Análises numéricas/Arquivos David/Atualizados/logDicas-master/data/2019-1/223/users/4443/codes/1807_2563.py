from numpy import * #importa a biblioteca para se trabalhar com vetores
medias = array(eval(input("Digite as notas dos estudantes: "))) #entrada das medias dos estudantes

while(size(medias) > 1): #o laco while eh necessaria para se repetir a pergunta indefinidamente
	aprovado = 0 #contador de aprovados, nota > 5
	mon = 0 #contador de monitores, nota > 7
	for nota in medias: #leitura diretamente de cada nota, e nao do indice
		if(nota >= 5): #verifica se a nota aprova o estudante
			aprovado = aprovado + 1		#Se verdade, aprovado eh incrementada em 1
		if(nota >= 7): #verifica se o estudante tem nota para ser monitor 
			mon = mon+1 #se verdade, monitor eh incrementado em 1
	print(aprovado-mon) #a diferenca indica apenas os aprovados q nao sao monitores

	medias = array(eval(input("Digite as notas dos estudantes: "))) #repe		
		
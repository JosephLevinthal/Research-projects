from numpy import * #importa a biblioteca q trabalha com vetores
p = array(eval(input("Digite o numero de gols marcados: "))) #vetor dos  gols marcados
c = array(eval(input("Digite o humero de gols sofridos: "))) #Vetor dos gols sofridos

vs = zeros(3, dtype=int) #cria um vetor com 3 posicoes contendo 0 nessas posicoes

for i in range(size(p)): #eh necessario criar uma lista de indices e comparar indicie a indice
	if(p[i] > c[i]): # compara indice a indice
		vs[0] = vs[0]+1 #Se verdade, incrementa, se falso vai para a comparacao seguinte
	elif(p[i] == c[i]): # compara indice a indice
		vs[1] = vs[1]+1	#Se verdade, incrementa, se falso vai para a comparacao seguinte
	elif(p[i] < c[i]): 
		vs[2] = vs[2]+1 #Se verdade, incrementa, se falso vai para a comparacao seguinte

print(vs)			
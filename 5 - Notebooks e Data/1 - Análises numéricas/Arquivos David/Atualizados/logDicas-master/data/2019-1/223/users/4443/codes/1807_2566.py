from numpy import * #importa a biblioteca para trabalhar com vetores
ft = array(eval(input("Digite as faltas dos funcionarios: "))) #Vetor do historico de faltas
vs = zeros(6, dtype=float) #cria um vetor com 6 posicoes, contendo 0 nessas posicoes

for i in ft: #laco for: le diretamente o elemento
	if(i == 2): #testa a condicao, se verdade
		vs[0] = vs[0] + 1	#incrementa em 1		  
	elif(i == 3): #se falso, testa a condicao seguinte, se verdade
		vs[1] = vs[1] + 1	#incrementa em 1		  		  
	elif(i == 4): #se falso, testa a condicao seguinte, se verdade
		vs[2] = vs[2] + 1	#incrementa em 1		  		  
	elif(i == 5): #se falso, testa a condicao seguinte, se verdade
		vs[3] = vs[3] + 1 #incrementa em 1
	elif(i == 6): #se falso, testa a condicao seguinte, se verdade
		vs[4] = vs[4] + 1	#incrementa em 1	  
	elif(i == 7): #se falso, testa a condicao seguinte, se verdade
		vs[5] = vs[5] + 1 #incrementa em 1
total = sum(vs) #soma o total de faltas para todos os dias da semana
vp = vs*(100/total) #multiplica todos os elementos do vs pela a razao, q da a porcentagem de falta para cada dia da semana
for v in range(size(vp)): #para a aproximacao das casas decimais eh necessario
	vp[v] = round(vp[v], 1) #arredonda todas as posicoes em 1 casa deciaml
print(vp)	  
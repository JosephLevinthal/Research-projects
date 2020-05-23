from numpy import * #importa a biblioteca para trabalhar com vetores
mf = array(eval(input("Digite as medias finais dos estudantes: "))) #vetor de entrada das notas 
f = array(eval(input("Digite a frequencia dos estudantes: "))) #vetor da entrada de frequencias
ch = float(input("Digite a carga horaria da disciplina: ")) #variavel da CH

vs = zeros(3, dtype=int) #cria um vetor de 3 posicoes contendo zero nessas posicoes

for i in range(size(mf)): #como sao varios vetores eh necessario criar uma lista de indices
	if(mf[i] >= 5 and f[i] >= 0.75*ch): #Verifica se a condicao eh atendida, 
		vs[0] = vs[0] + 1 #se V incrementa a posicao do vetor vs
	elif(mf[i] < 5):	#se a anterior for falsa, faz uma segunda comparacao
		vs[1] = vs[1] + 1 #se V incrementa a posicao do vetor vs
	elif(f[i] < 0.75*ch): #se a anterior for falsa, faz uma terceira comparacao
		vs[2] = vs[2] + 1	#se V incrementa a posicao do vetor vs
print(vs)		
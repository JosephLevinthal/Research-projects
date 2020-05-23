from numpy import *
vz = array(eval(input("Digite um vetor de numeros inteiros: "))) #definicao do vetor inicial
i = 0 #variavel contadora
z = 0 #tamanho do vetor de numeros postivos
while(i < len(vz)): #leitura de todas as posicoes do vetor vz 
	if(vz[i] >=0): # testa a posicao v[i]
		z = z+1 #se v[i] for maior q zero, incrementa a var acumuladora dos n positivos 
	i = i+1	 #incremento da variavel acumuladora
z = z 
pe = 0 #contador de posicao do vetor de entrada
ps = 0 #contador de posicao do vetor de entrada, eles devem ser defasados, pois o vetor de iteiros e menor do que o vetor de entrada, as posicoes não sao correspondentes
vs = zeros(z, dtype=int) #definicao do tamho do vetor de saida, de tamho z (qntidade de el positivos) e tipo inteiros
while(pe < len(vz)): #percorre todas as posicoes do vetor de entrada
	if(vz[pe] >= 0): #testa se o valor na posica vz[i] e maior ou igual a zero
		vs[ps] = vz[pe] #se verdade, o vetor de saida passa a ter esse valor
		pe = pe+1 #incrementa o contador do vetor de entrada
		ps = ps+1 #incrementa o contador do vetor de entrada
	else:	#se falso, isto e vz[i] < zero
		pe = pe+1 #incrementa o vetor de entrada, isto e, le p proximo valor
		ps = ps #nao incrementa o vetor de saida, fica aguardando o proximo valor positivo
print(vs) #imprime

#	forma alternativa
#while(pe < len(vz)):
#	if(vz[pe] >= 0):
#		vs.appened(vz[pe])

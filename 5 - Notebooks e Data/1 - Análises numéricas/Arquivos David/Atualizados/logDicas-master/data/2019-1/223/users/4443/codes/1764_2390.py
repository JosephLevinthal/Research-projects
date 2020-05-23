from numpy import *
pre = array(eval(input("Digite o numero de presentes a cada mes: "))) #informacao dos estudantes presentes
falt = array(eval(input("Digite o numero de faltantes a cada mes: "))) #informaco dos faltantes
freq = pre - falt #frequencia mensal
mes = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) #vetor contendo os 12 meses
i = 0
while(freq[i] != max(freq)): #procura o maior valor, posicao a posicao
	i = i+1 #se o valor não for encontrado, adiciona-se 1 na variavel contadora, e busca-se novamente
print(mes[i]) #se for encontado, sai do laco e imprime o mes
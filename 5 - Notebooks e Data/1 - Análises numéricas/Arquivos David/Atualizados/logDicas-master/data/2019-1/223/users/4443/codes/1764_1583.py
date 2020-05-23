from numpy import *
n = input("Digite uma sequencia de numeros: ") #os dados numericos digitados sao ligos como string
vec = "" #vetor vazio
i = 0 #variavel contadora do laco
while(i<len(n)): #i percorre todas as posicoes do vetor de entrada
	ini = i #inicia na posicao zero
	fim = i+3 #e conta mais 3 posicoes
	vec = vec + n[ini:fim]+"." #adiciona os primeiros 3 digtos ao vetor vazio e adiciona o ponto no final
	i = i+3 #i e incrementado em mais 3 posicoes
print(vec[:-1]) #imprime todos os valores, com excecao do ultimo, que é 


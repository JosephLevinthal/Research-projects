from numpy import*
g=array(eval(input("digite um vetor com o numeros de gols efetuados por partida: ")))
ga=array(eval(input("digite um vetor com o numeros de gols efetuados por partida: ")))
cont=zeros(3, dtype=int)
for i in range(size(g)):
	
	if(g[i]>ga[i]):
		cont[0]=cont[0]+1
	if(g[i]<ga[i]):
		cont[2]=cont[2]+1
	if(g[i]==ga[i]):
		cont[1]=cont[1]+1
print(cont)		
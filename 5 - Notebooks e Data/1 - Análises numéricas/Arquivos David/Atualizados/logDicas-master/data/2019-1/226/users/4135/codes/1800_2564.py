from numpy import*
#vetor para gols da partida
vet=array(eval(input("Digite o vetor de gols: ")))
#vetor para gols do time adversário
vet1=array(eval(input("Digite o vetor de gols: ")))
#vetor de contagem
cont=zeros(3, dtype=int)
for i in range(size(vet)):
	if(vet[i]>vet1[i]):
		cont[0]=cont[0]+1
	elif(vet[i]==vet1[i]):
		cont[1]=cont[1]+1
	elif(vet[i]<vet1[i]):
		cont[2]=cont[2]+1
print (cont)		
from numpy import *
vet1=array(eval(input("digite o numero de gols efetuados por este time em cada partida:")))
vet2=array(eval(input("digite o numero de gols efetuados pelo time adverssario:")))
cont=zeros(3, dtype=int)
for i in range(size(vet1)):
	if(vet1[i]>vet2[i]):
		cont[0]=cont[0]+1
	if(vet1[i]<vet2[i]):
		cont[2]=cont[2]+1
	if(vet1[i]==vet2[i]):
		cont[1]=cont[1]+1
print(cont)
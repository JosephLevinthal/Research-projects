from numpy import*
from numpy.random import*
dado=randint(1,7,size=6000)
cont=zeros(6,dtype=int) #vetor comeca do 0 e tem tamanho 6
for i in range (size(dado)):
	if(dado[i]==1):
		cont[0]=cont[0]+1
	if(dado[i]==2):
		cont[1]=cont[1]+1
	if(dado[i]==3):
		cont[2]=cont[2]+1
	if(dado[i]==4):
		cont[3]=cont[3]+1
	if(dado[i]==5):
		cont[4]=cont[4]+1
	if(dado[i]==6):
		cont[5]=cont[5]+1
print(cont)
from numpy import *
vet1=array(eval(input("digite")))  #vetor numero de gols de um time numea partida (i)
vet2=array(eval(input("digite")))   #vetor numero de gols contras de um time numa partida(i)
resultado=zeros(3,dtype=int)
for i in range(size(vet1)):
	if(vet1[i]> vet2[i]):
		resultado[0] = resultado[0] +1
	elif(vet1[i] == vet2[i]):
		resultado[1]= resultado[1] +1
	else:
		resultado[2]= resultado[2] +1
print(resultado)
		
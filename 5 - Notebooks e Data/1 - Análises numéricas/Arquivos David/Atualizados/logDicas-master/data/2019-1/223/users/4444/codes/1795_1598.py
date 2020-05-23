from numpy import *
vetor=array(eval(float(input('digite:   ')))
i=0
while(i < len(vetor)):
	if(vetor[i]>80):
		vetor[i]=vetor[i] - 5
		i=i+1
	else:
		vetor[i]=vetor[i]
		i=i+1
		
print(sum(round(vetor,2)))				

		
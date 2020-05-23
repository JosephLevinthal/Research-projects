from numpy import *
vetor = array(eval(input()))
negativo = 0
positivo = 0
i = 0
while(i<size(vetor)):
	if(vetor[i]<0):
		negativo = negativo + 1
	else:
		positivo = positivo +1
	i = i + 1
#print(negativo)
#print(positivo)

novovetor = arange(positivo)
j = 0
i = 0
while(i<size(vetor)):
	
	if(vetor[i]>=0):
		novovetor[j] = vetor[i]
		#print("i",i)
		#print(vetor[i])
		j = j +1
	i = i +1
	
print(novovetor)
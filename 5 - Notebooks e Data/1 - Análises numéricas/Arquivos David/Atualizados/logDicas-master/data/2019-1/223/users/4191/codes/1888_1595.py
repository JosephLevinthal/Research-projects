from numpy import *

vetor=array(eval(input("Vetor de notas: ")))
b=size(vetor)
a=0
soma=0
for i in range(size(vetor)):
	
	if(vetor[i]==min(vetor)and(a<1)):
		a=a+1
	else:
		soma=soma+vetor[i]
		
		

media=soma/(size(vetor)-1)
print(round(media, 2))
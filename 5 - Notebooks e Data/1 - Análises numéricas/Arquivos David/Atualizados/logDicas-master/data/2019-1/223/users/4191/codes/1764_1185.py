from numpy import *

vetor=array(eval(input("numeros: ")))
cont=0
i=0
diabete=0
while(cont<size(vetor)):
	if(vetor[i]>99):
		print(i)
		diabete=diabete+1
	else:
		i=i
	cont=cont+1
	i=i+1
print(diabete)		
	
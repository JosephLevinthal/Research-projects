from numpy import *

vetor=array(eval(input("Vetor: ")))
	
cont=0
media=0

while(cont<size(vetor)):
	media=((media+vetor[cont]**1/6) /size(vetor))**6
	cont=cont+1

print(round(media, 2))
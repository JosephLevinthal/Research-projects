from numpy import *

vetor=array(eval(input("Vetor: ")))

while(size(vetor) != 1):
	aprovados=0
	
	foror elemento in vet:
		if(elemento<7)and(elemento>=5):
			aprovados=aprovados+1
	
	print(aprovados)
	
	vetor=array(eval(input("Vetor: ")))
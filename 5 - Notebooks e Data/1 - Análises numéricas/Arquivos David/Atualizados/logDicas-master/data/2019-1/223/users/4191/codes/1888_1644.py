from numpy import *

vetor=array(eval(input("Notas: ")))
reprovado=0
for i in range(size(vetor)):
	if(vetor[i]<5):
		reprovado=reprovado +1
		
a=zeros(reprovado, dtype=int)		
b=0
for j in range(size(vetor)):
	if(vetor[j]<5):
		a[b]=j
		b=b+1
		
		
	
print(reprovado)		
print(a)		
from numpy import *

vetor=array(eval(input("Vetor de saques: ")))
saque=0
for i in range(size(vetor)):
	if(vetor[i]<=50):
		saque=saque+1
		
print(saque)
vet=zeros(saque, dtype=int)		
b=0

for i in range(size(vetor)):
	if(vetor[i]<=50):
		vet[b]=i
		b=b+1

print(vet)	
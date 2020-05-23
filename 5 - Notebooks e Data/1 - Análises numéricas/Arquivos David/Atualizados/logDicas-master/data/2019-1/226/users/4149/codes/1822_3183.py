from numpy import*

vet=array(eval(input("entre como o vetor;")))


aux=0
j=-1
vetz=zeros(size(vet),dtype=int)
for i in range(size(vet)):
	vetz[aux]=vet[j]
	aux=aux+1
	j=j-1
print(vet)


	
	

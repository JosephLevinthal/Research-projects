from numpy import*

vet=array(eval(input("entre com o vetor:")))

zero=zeros(size(vet),dtype=int)
j=0
for i in range(size(vet)):
	if(vet[i]>= 5):
		j=j+1
print(j)
a=0
z=zeros(j,dtype=int)
for x in range(size(vet)):
	if(vet[x]>=5):
		z[a]=x		
		a=a+1
print(z)			
			


	
			
	

from numpy import *

vet=array(eval(input("Vetor: ")))
v=zeros(6)

for i in range(size(vet)):
	
	if(vet[i]==2):
		v[0]=v[0]+1
	if(vet[i]==3):
		v[1]=v[1]+1
	if(vet[i]==4):
		v[2]=v[2]+1
	if(vet[i]==5):
		v[3]=v[3]+1
	if(vet[i]==6):
		v[4]=v[4]+1
	if(vet[i]==7):
		v[5]=v[5]+1
		
for i in range(size(v)):
	v[i]=round(v[i]/size(vet)*100, 1)
	
print(v)	

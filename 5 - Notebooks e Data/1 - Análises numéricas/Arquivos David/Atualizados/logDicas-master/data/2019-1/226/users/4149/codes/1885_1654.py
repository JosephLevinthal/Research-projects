from numpy import*
from numpy.linalg import*
s=input("entre:")
a= s.split(",")
vet=zeros(5,dtype=int)
vet1=zeros(5,dtype=int)
vet2=zeros(5,dtype=int)
vet3=zeros(5,dtype=int)
vet4=zeros(5,dtype=int)

for i in range(size(a)):
	if(a[i]=="AM"):
		vet[0]=vet[0]+1
for i in range(size(a)):
	if(a[i]=='PE'):
		vet1[1]=vet1[1]+1
for i in range(size(a)):
	if(a[i]=="MG"):
		vet2[2]=vet2[2]+1
for i in range(size(a)):
	if(a[i]=="SP"):
		vet3[3]=vet3[3]+1
for i in range(size(a)):
	if(a[i]=="RS"):
		vet4[4]=vet4[4]+1
		
d=vet+vet1+vet2+vet3+vet4
print(max(d))
print(d)



		




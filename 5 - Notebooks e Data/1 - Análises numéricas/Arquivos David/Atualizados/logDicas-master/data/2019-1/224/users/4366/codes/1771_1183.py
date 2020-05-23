from numpy import*
vet=array(eval(input("digite um vetor:")))
i=0
b=0
while(i<size(vet)):
	if(vet[i])>=0:
		b=b+1
	else:
		b=b+0
	i=i+1
ii=0
iii=0
z=zeros(b,dtype)
while(iii<b):
	if(vet[ii]>=0):
		z[iii]=vet[ii]
		ii=ii+1
		iii=iii+1
	else:
		ii=ii+1
		iii=iii+0
print(z)

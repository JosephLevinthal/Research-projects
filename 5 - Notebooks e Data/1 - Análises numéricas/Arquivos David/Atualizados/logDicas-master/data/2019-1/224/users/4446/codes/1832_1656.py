from numpy import *
s=input("pais origem: ")
s=s.split(',')
b=0
e=0
f=0
it=0
pt=0
for i in s:
	if(i=="BE"):
		b=b+1
	if(i=="ES"):
		e=e+1
	if(i=="FR"):
		f=f+1
	if(i=="IT"):
		it=it+1
	if(i=="PT"):
		pt=pt+1
vet=zeros(5, dtype=int)
vet[0]=b
vet[1]=e
vet[2]=f
vet[3]=it
vet[4]=pt
print(max(vet))
print(vet)
	

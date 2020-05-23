from numpy import *
s=array(eval(input("digite as preferencias: ")))
a=0
b=0
c=0
for elemento in s:
	elemento=elemento.upper()
	if(elemento=="TV"):
		a=a+1
	if(elemento=="NETFLIX"):
		b=b+1
	if(elemento=="YOUTUBE"):
		c=c+1
vet=zeros(3, dtype=int)
vet[0]=a
vet[1]=b
vet[2]=c
print(vet)
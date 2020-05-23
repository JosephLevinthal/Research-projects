from numpy import *
vet=array(eval(input("digite quando faltou: ")))
f=zeros(6, dtype=float)
d2=0
d3=0
d4=0
d5=0
d6=0
d7=0
for elemento in vet:
	if(elemento==2):
		d2=d2+1
	if(elemento==3):
		d3=d3+1
	if(elemento==4):
		d4=d4+1
	if(elemento==5):
		d5=d5+1
	if(elemento==6):
		d6=d6+1
	if(elemento==7):
		d7=d7+1
pd2=round(((d2/size(vet))*100), 1)
pd3=round(((d3/size(vet))*100), 1)
pd4=round(((d4/size(vet))*100), 1)
pd5=round(((d5/size(vet))*100), 1)
pd6=round(((d6/size(vet))*100), 1)
pd7=round(((d7/size(vet))*100), 1)
f[0]=pd2
f[1]=pd3
f[2]=pd4
f[3]=pd5
f[4]=pd6
f[5]=pd7
print(f)
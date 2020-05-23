from numpy import *
falta=array(eval(input("digite o numero de faltas dos dias da semana:")))
cont=zeros(6,dtype=int)
for i in range(size(falta)):
	if(falta[i]==2):
		cont[0]=cont[0]+1
	if(falta[i]==3):
		cont[1]=cont[1]+1
	if(falta[i]==4):
		cont[2]=cont[2]+1
	if(falta[i]==5):
		cont[3]=cont[3]+1
	if(falta[i]==6):
		cont[4]=cont[4]+1
	if(falta[i]==7):
		cont[5]=cont[5]+1
vp=zeros(6,dtype=float)
for i in range(size(vp)):
	vp[i]=round((cont[i]/size(falta))*100, 1)
print(vp)
		
		
		
		
		
		
		
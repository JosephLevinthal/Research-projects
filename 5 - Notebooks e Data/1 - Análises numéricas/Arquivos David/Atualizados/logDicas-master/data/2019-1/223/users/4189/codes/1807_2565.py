from numpy import * 
media = array(eval(input("aprovados:")))
pres = array(eval(input("reprovados:")))
carga = int(input("carga horaria:"))
nvet = zeros(3,dtype=int)
for i in range(0,size(media)):
	if(media[i]>=5) and (pres[i]>= 0.75*carga):
		nvet[0]=nvet[0]+1
	if(media[i]<5) and ( pres[i]>= 0.75*carga):
		nvet[1]=nvet[1]+1
	if(pres[i]< 0.75*carga):
		nvet[2]=nvet[2]+1
print(nvet)

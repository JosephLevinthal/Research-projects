from numpy import *
vet1=array(eval(input("Medias: ")))
vet2=array(eval(input("Presenca: ")))
ch=int(input("Carga horaria: "))

vet3=zeros(3, dtype=int)

for i in range(size(vet1)):
	if (vet1[i]>=5 and vet2[i] >= (ch*(75/100))):
		vet3[0]=vet3[0]+1
	if (vet1[i]<5):
		vet3[1]=vet3[1]+1
	if (vet2[i]<(ch*(75/100))):
		vet3[2]=vet3[2]+1

print(vet3)
		
		
		
	
		
		




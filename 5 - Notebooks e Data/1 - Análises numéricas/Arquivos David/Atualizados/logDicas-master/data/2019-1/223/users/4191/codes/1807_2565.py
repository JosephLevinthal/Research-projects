from numpy import *

media=array(eval(input("Media: ")))

horas=array(eval(input("horas: ")))

carga=int(input("Carga horaria: "))

vet=zeros(3, dtype=int)
for i in range(size(media)):
	
	if(media[i]>=5)and(horas[i]/carga >= 0.75):
		vet[0]=vet[0]+1
		
	elif(media[i]<5)and(horas[i]/carga >= 0.75):
		vet[1]=vet[1]+1
	elif(horas[i]/carga < 0.75):
		vet[2]=vet[2]+1
		
print(vet)		
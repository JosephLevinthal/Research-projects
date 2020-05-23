from numpy import *

gols=array(eval(input("Gols por partida: ")))

tomou=array(eval(input("Gols tomados por partida: ")))


vitoria=0
empate=0
derrota=0



for i in range(size(gols)):
	if(gols[i]>tomou[i]):
		vitoria=vitoria+1
	elif(gols[i]<tomou[i]):
		derrota=derrota+1
	elif(gols[i]==tomou[i]):
		empate=empate+1
		
	
		
vet=zeros(3, dtype=int)		
		
vet[0]=vitoria
vet[1]=empate
vet[2]=derrota		

print(vet)
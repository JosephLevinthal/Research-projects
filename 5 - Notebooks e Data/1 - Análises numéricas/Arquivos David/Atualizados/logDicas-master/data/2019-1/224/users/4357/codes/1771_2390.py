from numpy import*
presenca=array(eval(input("digite:")))
falta=array(eval(input("digite:")))
frequencia=presenca-falta
i=0
while(i<size(frequencia)):
	if(frequencia[i]==max(frequencia)):
		print(i+1)
	i=i+1
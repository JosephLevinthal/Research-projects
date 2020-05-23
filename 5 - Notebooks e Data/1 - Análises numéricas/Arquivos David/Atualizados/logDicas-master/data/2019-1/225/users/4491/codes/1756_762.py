from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

data= input()

dia = ""+data[0]+data[1]
mes= ""+data[2]+data[3]
ano =""+data[4:]

indice_mes= int(mes)-1

i=0
while(i<size(vet_mes)):
	if(i == indice_mes):
		extenso_mes=vet_mes[i]
	
	i= i+1

print(dia, "de", extenso_mes, "de", ano)
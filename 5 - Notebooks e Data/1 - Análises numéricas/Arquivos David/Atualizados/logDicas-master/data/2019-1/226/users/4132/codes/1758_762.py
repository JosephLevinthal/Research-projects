from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
v = input("vai que: ")

mes = v[2:4]
intmes = int(mes)
i=0

while(i<size(vet_mes)):
	if(i+1==intmes):
		mes=vet_mes[i]
	i=i+1
	
data = v[0:2]+" de "+mes+" de "+v[4:]
print(data)
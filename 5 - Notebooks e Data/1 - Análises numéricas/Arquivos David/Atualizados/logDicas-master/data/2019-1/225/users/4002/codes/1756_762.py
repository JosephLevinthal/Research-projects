from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
string = input("")
print(string[0:2],"de",vet_mes[(int(string[2])*10+int(string[3]))-1],"de",string[4::])


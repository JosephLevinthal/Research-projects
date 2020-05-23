from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data = input("Informe a data (dd/mm/aaaa): ")
dia = data[:2]
mes = int(data[2:4])
ano = data[-4:]

if(mes == 1):
	a = vet_mes[0]
elif(mes == 2):
	a = vet_mes[1]
elif(mes == 3):
	a = vet_mes[2]
elif(mes == 4):
	a = vet_mes[3]
elif(mes == 5):
	a = vet_mes[4]
elif(mes == 6):
	a = vet_mes[5]
elif(mes == 7):
	a = vet_mes[6]
elif(mes == 8):
	a = vet_mes[7]
elif(mes == 9):
	a = vet_mes[8]
elif(mes == 10):
	a = vet_mes[9]
elif(mes == 11):
	a = vet_mes[10]
elif(mes == 12):
	a = vet_mes[11]


print(dia,"de",a,"de",ano)

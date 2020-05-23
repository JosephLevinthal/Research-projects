from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

data=input("Data: ")

b=int(data[2:4])

if(b==1):
	mes=vet_mes[0]
elif(b==2):
	mes=vet_mes[1]
elif(b==3):
	mes=vet_mes[2]
elif(b==4):
	mes=vet_mes[3]
elif(b==5):
	mes=vet_mes[4]
elif(b==6):
	mes=vet_mes[5]
elif(b==7):
	mes=vet_mes[6]
elif(b==8):
	mes=vet_mes[7]
elif(b==9):
	mes=vet_mes[8]
elif(b==10):
	mes=vet_mes[9]
elif(b==11):
	mes=vet_mes[10]
elif(b==12):
	mes=vet_mes[11]
	
print(data[0:2],' de ', mes, ' de ', data[4:9])

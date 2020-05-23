from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
n = input("Numero: ")
new = int(n[2:4])
i = 0

if(new == 1):
	mes = 0
elif(new == 2):
	mes = 1
elif(new == 3):
	mes = 2
elif(new == 4):
	mes = 3
elif(new == 5):
	mes = 4
elif(new == 6):
	mes = 5
elif(new == 7):
	mes = 6
elif(new == 8):
	mes = 7
elif(new == 9):
	mes = 8
elif(new == 10):
	mes = 9
elif(new == 11):
	mes = 10
else:
	(new == 12)
	mes = 11
	
print(n[0:2], "de", vet_mes[mes], "de", n[4:])	
	
		
		
		
		
		
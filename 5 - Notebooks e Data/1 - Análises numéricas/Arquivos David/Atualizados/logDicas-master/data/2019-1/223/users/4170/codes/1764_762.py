from numpy import *
# Vetor contendo o nome dos meses do ano
v = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data = input("Informe a data: ")
dia = data[:2]
mes = int(data[2:4])
ano = data[-4:]
if(mes == 1):
	a = v[0]
elif(mes == 2):
	a = v[1]
elif(mes == 3):
	a = v[2]
elif(mes == 4):
	a = v[3]
elif(mes == 5):
	a = v[4]
elif(mes == 6):
	a = v[5]
elif(mes == 7):
	a = v[6]
elif(mes == 8):
	a = v[7]
elif(mes == 9):
	a = v[8]
elif(mes == 10):
	a = v[9]
elif(mes == 11):
	a = v[10]
elif(mes == 12):
	a = v[11]
print(dia, "de", a, "de", ano)
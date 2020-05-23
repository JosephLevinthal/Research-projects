from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
s = int(input("digite 8 numeros: "))
if s[2:3] == 1:
	dia = s[0:1]
	mes = janeiro
	ano = s[4,5,6,7]
print(dia + " " + "de" + " " + mes + " " + "de" + " " + ano)
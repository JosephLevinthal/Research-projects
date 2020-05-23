from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho',
					  'julho', 'agosto', 'setembro','outubro', 'novembro', 'dezembro'])

data = input("data (ddmmaaaa):")
dd = (data[:2])
mm = (data[2:4])
aaaa = (data[4:])

p=vet_mes[int(data[2:4])-1]

print(dd , "de" , p , "de", aaaa)

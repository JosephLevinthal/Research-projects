from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
dat = input("insira dia, dd/mm/aaaa:")

dia =(dat[0:2])
mes =(dat[2:4])
ano = (dat[4:])


extra = int(mes)-1

print(dia ,"de", vet_mes[extra] ,"de", ano)





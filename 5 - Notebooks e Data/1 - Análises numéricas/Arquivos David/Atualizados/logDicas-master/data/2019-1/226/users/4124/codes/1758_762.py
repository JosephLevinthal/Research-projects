from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data =input("Digite uma data: ")
dd = data[0:2]
mm = data[2:4]
aaaa = data[4:8]

mes = vet_mes[int(mm) - 1]
print(dd, "de", mes, "de", aaaa)
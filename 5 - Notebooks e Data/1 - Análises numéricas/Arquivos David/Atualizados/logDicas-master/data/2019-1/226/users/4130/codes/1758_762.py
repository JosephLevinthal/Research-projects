from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

data = input("Entre com a data: ")

dd = data[0:2]
mm = data[2:4]
aaaa = data[4:8]

mes_ext = vet_mes[int(mm) - 1]

print(dd, "de", mes_ext, "de", aaaa)
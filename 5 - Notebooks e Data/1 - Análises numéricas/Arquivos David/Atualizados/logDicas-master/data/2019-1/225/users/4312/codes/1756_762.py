from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data = input("Insira um valor: ")

dia = data[:2]
mes = int(data[2:4])
ano = data[-4:]

mes_ = vet_mes[mes -1]

nova_data = dia +  " de " + mes_ + " de " + ano
print(nova_data)
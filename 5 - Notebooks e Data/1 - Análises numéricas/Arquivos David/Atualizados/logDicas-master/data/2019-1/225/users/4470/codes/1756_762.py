from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
a=input("Digite:")
dd=(a[0:2])
mes=(a[2:4])
aaaa=(a[4:])
int(a[2:4])
mm=vet_mes[int(a[2:4])-1]
print(dd+" de "+mm+" de "+aaaa)
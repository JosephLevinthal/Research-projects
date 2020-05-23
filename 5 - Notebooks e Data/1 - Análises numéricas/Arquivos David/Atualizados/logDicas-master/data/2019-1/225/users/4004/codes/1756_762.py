from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
t = str(input("data por extenso: (ddmmaaaa) "))

dd = t[:2]
aaaa = t[-4:]
n = int(t[2] + t[3])
n = n - 1
mm = vet_mes[n]
print(dd, "de", mm, "de", aaaa )
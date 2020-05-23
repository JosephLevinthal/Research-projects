from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
s=input("Digite os caracteres: ")
 # Vetor contendo os dias do ano
dd=(s[0:2])
# Vetor contendo os meses do ano
mes=(s[2:4])
 # Vetor contendo o ano
aaaa=(s[4:])
# Vetor contendo os meses
int(s[2:4])

mm= vet_mes[int(s[2:4])-1]

print(dd + " de " + mm + " de " + aaaa)
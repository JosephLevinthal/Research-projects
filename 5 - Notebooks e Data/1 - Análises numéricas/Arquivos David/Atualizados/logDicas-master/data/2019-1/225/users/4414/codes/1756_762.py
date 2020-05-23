from numpy import *

vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
s = input("digite os carcteres:")

dd=(s[0:2])

mes=(s[2:4])

aaaa=(s[4:])

int(s[2:4])

mm= vet_mes[int(s[2:4])-1]

print(dd +" de " + mm + " de " + aaaa)

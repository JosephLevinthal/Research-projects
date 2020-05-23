from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
v = input("vai:")
dd= v[0] + v[1]
em = int(v[2])*10 + int(v[3]) -1
bb= v[4]+ v[5]+ v[6]+ v[7]
print(dd,"de",vet_mes[em],"de",bb)
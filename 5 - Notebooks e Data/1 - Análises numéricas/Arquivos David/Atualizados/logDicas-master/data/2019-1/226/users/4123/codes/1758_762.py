from numpy import *
# Vetor contendo o nome dos meses do ano
#n = str(input())
n = input()
mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
print(n[0]+n[1],"de",mes[int(n[2:4])-1],"de",int(n[4:]))
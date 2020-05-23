from numpy import *
# Vetor contendo o nome dos meses do ano
a = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
b = str(input('data: '))
print(b[0:2],'de',a[int(b[2:4])-1], 'de', b[4:9])
from numpy import *
vet = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
dt= input("digite a data: ")
dd=dt[0:2]
mm=dt[2:4]
an=dt[4:8]
me=vet[int(mm)-1]
print(dd,"de",me,"de",an)

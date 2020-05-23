from numpy import *
x=input("Digite uma string de 8 caracteres: ")
z=x[0:2]
y=x[2:4]
y=int(y)
y=y-1
g=x[4:8]
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
print(z,"de",vet_mes[y],"de",g)
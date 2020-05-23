from numpy import*
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
n=input("data:")
#Vetor contendo os dias do ano
x=(n[:2])
#vetor contendo os meses do ano
m=(n[2:4])
#vetor contendo o ano
w=(n[4:])
#vetor contendo os meses


y=vet_mes[int(n[2:4])-1]

j= x+ " de " +y +" de "+ w

print(j)
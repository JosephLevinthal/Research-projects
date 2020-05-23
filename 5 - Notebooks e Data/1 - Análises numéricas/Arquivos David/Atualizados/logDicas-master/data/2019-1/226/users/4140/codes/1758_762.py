from numpy import *
# Vetor contendo o nome dos meses do ano
v2= array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
v1=input()
a=int(v1)
a1=a//1000000
if(a1<10):
	a1=str(0)+str(a1)
a2=a%10000
a3=((a//10000)%100)-1
print(a1,"de",v2[a3],"de",a2)

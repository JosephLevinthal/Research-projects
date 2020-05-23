from numpy import *
vet=array(eval(input("digite as matriculas dos alunos: ")))

i=0
for elemento in vet:
	if(elemento%2!=0):
		i=i+1
g2=zeros(i, dtype=int)
i=0
for elemento in vet:
	if(elemento%2!=0):
		g2[i]=elemento
		i=i+1
print(g2)

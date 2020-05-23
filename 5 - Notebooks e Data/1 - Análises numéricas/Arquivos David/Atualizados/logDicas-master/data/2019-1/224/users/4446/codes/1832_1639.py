from numpy import *
vet=array(eval(input("digite a quantidade de alunos matriculados: ")))
p=0
j=0
pp=0
for i in vet:
	if(i%2==0):
		p=p+1
q=zeros(p, dtype=int)
for i in vet:
	if(i%2==0):
		q[j]=pp
		j=j+1
	pp=pp+1	
print(p)
print(q)
	
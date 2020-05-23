from numpy import *
aulas= array(eval(input("digite a frequencia :")))
alunos = size(aulas)
a = 0
for i in range(alunos):
	if(aulas[i]>= 70):
		a = a + 1
print(a)
af= zeros(a,dtype= int)
l = 0
for v in range(alunos):
	if(aulas[v]>= 70):
		af[l]= v
		l = l + 1
print(af)
	
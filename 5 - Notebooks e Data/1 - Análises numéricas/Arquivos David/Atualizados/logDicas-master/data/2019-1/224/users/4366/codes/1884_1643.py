from numpy import *
nota=array(eval(input("vetor de notas: ")))
alunos=size(nota)
a=0
for i in range(alunos):
	if (nota[i]>=5):
		a= a + 1
ap=zeros(a, dtype=int)
l=0
for v in range(alunos):
	if (nota[v]>=5):
		ap[l]=v
		l= l + 1
print(a)
print(ap)
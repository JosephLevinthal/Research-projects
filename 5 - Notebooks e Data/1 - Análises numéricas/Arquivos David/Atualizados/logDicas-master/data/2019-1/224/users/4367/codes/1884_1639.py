from numpy import*
t=array(eval(input("digite o vetor com o numero de alunos por turma: ")))
p=0
for i in range(size(t)):
	if(t[i]%2==0):
		p=p+1
print(p)
v=zeros(p, dtype=int)
g=0
b=0
for i in range (size(t)):
	if(t[i]%2==0):
		v[g]=v[g]+b
		g=g+1
	b=b+1
print(v)	
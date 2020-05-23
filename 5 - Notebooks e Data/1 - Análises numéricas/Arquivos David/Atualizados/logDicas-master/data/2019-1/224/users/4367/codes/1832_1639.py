from numpy import*
a=array(eval(input("digite o numero de alunos por turma: ")))
p=0
for i in a:
	if(i%2==0):
		p=p+1
print(p)
par=zeros(p, dtype=int)
b=0
for i in range (size(a)):
	if(a[i]%2==0):
		par[b]=par[b]+i
		b=b+1
print(par)
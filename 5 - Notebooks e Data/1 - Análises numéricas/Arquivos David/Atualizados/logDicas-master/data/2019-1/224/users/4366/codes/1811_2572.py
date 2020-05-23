from numpy import*
matr=array(eval(input("digite as matriculas dos alunos: ")))
grup2=0
for i in range(size(matr)):
	if(matr[i]%2!=0):
		grup2=grup2+1
v=zeros(grup2,dtype=int)
a=0
for i in range(size(matr)):
	if(matr[i]%2!=0):
		v[a]=v[a]+matr[i]
		a=a+1
print(v)
	
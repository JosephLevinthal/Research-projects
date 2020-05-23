from numpy import*
aluno=array(eval(input("digite o numero:")))
a=0
b=0
for i in aluno:
	if(i<70):
		a=a+1
q=zeros(a,dtype=int)
c=0
for j in aluno:
	if(j<70):
		q[b]=c
		b=b+1
	c=c+1
print(a)
print(q)

		
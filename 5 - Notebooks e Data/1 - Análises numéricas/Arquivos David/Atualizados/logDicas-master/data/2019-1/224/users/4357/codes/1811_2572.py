from numpy import*
aluno=array(eval(input("digite o numero:")))
a=0
for i in aluno:
	if(i%2 !=0):
		a=a+1
d=zeros(a,dtype=int)
b=0
for e in aluno:
	if(e%2!=0):
		d[b]=e
		b=b+1
print(d)

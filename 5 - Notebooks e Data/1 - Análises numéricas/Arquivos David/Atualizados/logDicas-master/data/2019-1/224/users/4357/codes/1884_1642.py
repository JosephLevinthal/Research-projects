from numpy import*
vetor=array(eval(input("digite o numero:")))
a=0
d=0
for i in vetor:
	if(vetor[d]%5==0):
		a=a+1
	d=d+1
print(a)
indices=zeros(a,dtype=int)
d=0
t=0
for f in vetor:
	if(vetor[d]%5==0):
		indices[t]=d
		t=t+1
	d=d+1
print(indices)
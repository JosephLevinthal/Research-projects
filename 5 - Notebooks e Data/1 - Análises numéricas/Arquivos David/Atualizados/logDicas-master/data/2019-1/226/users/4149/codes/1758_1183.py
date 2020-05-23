from numpy import*
vet=array(eval(input("entre com o vetor")))
i=0
p=0
while(i<size(vet)):
	if(vet[i]>=0):
		p=p+1
	i=i+1	
e=0
s=0
v=zeros(p,dtype=int)
while(e<size(vet)):
	if(vet[e]>0):
		v[s]=vet[e]
		s=s+1
	e=e+1
print(v)

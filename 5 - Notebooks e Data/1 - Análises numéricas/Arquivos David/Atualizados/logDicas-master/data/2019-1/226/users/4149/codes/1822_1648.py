from numpy import*

f=array(eval(input("entre com o vetor:")))

p=0

for i in range(size(f)):
	if(f[i]<70):
		p=p+1

print(p)

vet=zeros(p,dtype=int)

b=0
for y in range(size(f)):
	if(f[y]<70):
		vet[b]=f[y]
		b=b+1
vet2=zeros(size(vet),dtype=int)	
x=0
for i in range(size(f)):
	if(f[i]<70):
		vet2[x]=i
		x=x+1
print(vet2)
		

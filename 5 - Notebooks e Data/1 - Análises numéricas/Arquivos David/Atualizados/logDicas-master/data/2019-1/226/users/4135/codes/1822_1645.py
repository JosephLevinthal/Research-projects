from numpy import*
v=array(eval(input("Digite o vetor de saque: ")))
i=0
for y in range(0,size(v)):
	if(v[y]>=2000):
		i=i+1
print(i)

n=size(v)
c=zeros(n,dtype=int)
for x in range(0,size(v)):
	p=0
	if(v[x]>=2000):
		c[0]=p
		c[x]=x
c[0]=p
c[x]

print()			
	
	
	
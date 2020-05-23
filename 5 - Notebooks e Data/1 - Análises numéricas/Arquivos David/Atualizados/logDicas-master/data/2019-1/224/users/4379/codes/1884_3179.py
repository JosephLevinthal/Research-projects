from numpy import*
u=array(eval(input("digite o vetor: ")))
v=zeros(size(u), dtype=int)
c=0
for i in range(size(u)):
	if(u[i]!=1):
		v[c]=v[c]+u[i]
		c=c+1
for i in range(size(u)):
	if(u[i]==1):
		v[c]=v[c]+u[i]
		c=c+1
print(v)

	
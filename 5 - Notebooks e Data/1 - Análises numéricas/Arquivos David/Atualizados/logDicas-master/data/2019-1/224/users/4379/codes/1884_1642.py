from numpy import*
v=array(eval(input("digite o vetor: ")))
i=0
e=0
for i in range(size(v)):
	if(v[i]%5==0):
		e=e+1	
c=zeros(e, dtype=int)
s=0
p=0
for i in range(size(v)):
	if(v[i]%5==0):
		c[p]=c[p]+s
		p=p+1
	s=s+1
print(e)
print(c)





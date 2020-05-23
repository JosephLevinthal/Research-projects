from numpy import*
v=array(eval(input("entre com o vetor:")))
b=0
for i in v:
	if(i%2!=0):
		b=b+1
p=zeros(b,dtype=int)
x=0
g=0
for s in v:
	if(s%2 != 0):
		p[x]=v[g]
		x=x+1
	g=g+1
print(p)
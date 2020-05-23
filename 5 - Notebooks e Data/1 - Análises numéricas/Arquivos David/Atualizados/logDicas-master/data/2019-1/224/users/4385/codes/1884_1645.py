from numpy import *
t=array(eval(input("diga o valor: ")))
p=0
for i in range(size(t)):
	if(t[i]>=2000):
		p=p+1
print(p)
v=zeros(p,dtype=int)
g=0
b=0
for i in range(size(t)):
	if(t[i]>=2000):
		v[g]=b
		g=g+1
	b=b+1
print(v)
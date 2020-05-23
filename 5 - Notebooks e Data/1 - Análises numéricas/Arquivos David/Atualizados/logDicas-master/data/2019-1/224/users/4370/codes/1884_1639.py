from numpy import *
t= array(eval(input("digite o valor das turmas")))
j=0
for i in range(size(t)):
	if(t[i]%2==0):
		j=j+1
print(j)
v=zeros(j,dtype=int)
g=0
b=0
for i in range (size(t)):
	if(t[i]%2==0):
		v[g]=v[g]+b
		g=g+1
	b=b+1
print(v)


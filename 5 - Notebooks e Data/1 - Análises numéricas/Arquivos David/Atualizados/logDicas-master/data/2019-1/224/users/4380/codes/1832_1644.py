from numpy import *
v=array(eval(input("Notas: ")))
p1=0
p2=0
soma=0
for p1 in v:
	if(p1<5.0):
		soma=soma+1
indrp=zeros(soma,dtype=int)
k=0
for i in range(size(v)):
	if (v[i]<5.0):
		indrp[k]=i
		k=k+1
print(soma)
print(indrp)
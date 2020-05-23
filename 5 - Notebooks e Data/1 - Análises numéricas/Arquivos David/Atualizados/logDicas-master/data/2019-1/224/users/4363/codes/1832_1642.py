from numpy import *
t=array(eval(input("numero de launos")))
p=0 
for v in t:
	if(v%5==0):
		p=p + 1
vp=zeros(p, dtype=int)
i=0
c=0
for v in t:
	if(v%5==0):
		vp[i]=c
		i=i+1
	c=c+1
print(p)
print(vp)
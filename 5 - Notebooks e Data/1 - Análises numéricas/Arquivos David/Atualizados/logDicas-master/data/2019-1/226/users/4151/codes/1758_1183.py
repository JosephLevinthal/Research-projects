from numpy import*
v=array(eval(input("digite: ")))
i=0
p=0
while(i<size(v)):
	if(v[i]>=0):
		p=p+1
	i=i+1
	
v1=zeros(p,dtype=int)
t=0
i=0
while(t<size(v)):
	if(v[t]>=0):
		v1[i]=v[t]
		i=i+1
	t=t+1
print(v1)
	
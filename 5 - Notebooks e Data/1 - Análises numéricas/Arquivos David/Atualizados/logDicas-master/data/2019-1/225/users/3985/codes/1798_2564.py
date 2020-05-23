from numpy import*

v=array(eval(input()))
u=array(eval(input()))
a=0
e=0
d=0
vr = zeros(3,dtype=int)
i = 0
while (i < size(v)):
	if(size(v)>0)and(size(u)>0):
		if (v[i]>u[i]):
			a=a+1
		elif (v[i]==u[i]):
			e=e+1
		elif (v[i]<u[i]):
			d=d+1
	i = i + 1
	
vr[0]=a
vr[1]=e
vr[2]=d
print(vr)
from numpy import*
v=array(eval(input("digite o numero:")))
i=0
e=0
while(i<size(v)):
	if(v[i]>=0):
		e=e+1
	else:
		e=e+0
	i=i+1
a=0
b=0
z=zeros(e,dtype=int)
while(b<e):
	if(v[a]>=0):
		z[b]=v[a]
		a=a+1
		b=b+1
	else:
		a=a+1
		b=b+0
print(z)
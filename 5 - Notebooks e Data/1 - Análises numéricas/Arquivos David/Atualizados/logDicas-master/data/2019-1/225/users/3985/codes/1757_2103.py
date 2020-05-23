from numpy import*

a=array(eval(input()))
b=array(eval(input()))
x=size(b)-1
c=zeros(size(b),dtype=int)
y=0
while(x>=0):
	c[y]=b[x]
	y+=1
	x-=1
b = c
d=0
while(d<size(b)):
	if(a[d] > b[d]):
		print(a[d])
	elif(b[d]>a[d]):
		print(b[d])
	d+=1
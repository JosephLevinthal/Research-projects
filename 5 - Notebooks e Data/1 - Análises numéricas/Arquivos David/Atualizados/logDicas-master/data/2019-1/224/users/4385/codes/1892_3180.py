from numpy import*
v=array(eval(input("digite: ")))
a=0
b=0
c=0
d=0
z=zeros(4,dtype=int)
for i in range(size(v)):
	if(v[i]==1):
		a=a+1
	if(v[i]==2):
		b=b+1
	if(v[i]==3):
		c=c+1
	if(v[i]==4):
		d=d+1
z[0]=a
z[1]=b
z[2]=c
z[3]=d
print(z)

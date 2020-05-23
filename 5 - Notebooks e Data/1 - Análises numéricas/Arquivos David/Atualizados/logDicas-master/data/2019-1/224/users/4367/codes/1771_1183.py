from numpy import*
a=array(eval(input("digite seus elementos: ")))
i=0
b=0
while(i<size(a)):
	if(a[i])>=0:
		b=b+1
	else:
		b=b+0
	i=i+1
ii=0
iii=0
z=zeros(b, dtype)
while(iii<b):
	if(a[ii]>=0):
		z[iii]=a[ii]
		ii=ii+1
		iii=iii+1
	else:
		ii=ii+1
		iii=iii+0
print(z)
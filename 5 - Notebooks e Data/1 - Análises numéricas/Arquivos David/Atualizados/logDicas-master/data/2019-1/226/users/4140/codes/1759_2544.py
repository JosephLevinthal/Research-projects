from numpy import*
v1=array(eval(input()))
i=0
a=0
b=0
c=0
while(i<size(v1)):
	if(v1[i]>=10):
		a=a+1
	elif(v1[i]>=5 and v1[i]<10):
		b=b+1
	else:
		c=c+1
	i=i+1
print(a)
print(b)
print(c)
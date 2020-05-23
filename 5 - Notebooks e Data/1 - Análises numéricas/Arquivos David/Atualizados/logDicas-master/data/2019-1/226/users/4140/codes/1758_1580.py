from numpy import*
v1=array(eval(input()))
v2=array(eval(input()))
i=0
a=0
b=0
c=0
d=0
j=0
while(i<size(v1)):
	if(v1[i]==-1):
		a=a+1
	elif(v1[i]>=6):
		b=b+1
		d=d+v1[i]
	else:
		c=c+1
		d=d+v1[i]
	i=i+1
print(a)
print(b)
print(c)
print(round(d/(c+b),2))

while(v1[j]!=max(v1)):
	j=j+1
print(v2[j])
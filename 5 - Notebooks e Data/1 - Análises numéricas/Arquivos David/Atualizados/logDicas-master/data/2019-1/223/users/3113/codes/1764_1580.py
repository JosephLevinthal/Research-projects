from numpy import*
a=array(eval(input("")))
s=array(eval(input("")))

i=0
i1=0
i2=0
i3=0
m=0

while(i<size(a)):
	if(a[i]==-1):
		i1=i1+1
	if(6<=a[i]<=10):
		i2=i2+1
		m=m+a[i]
	if(0<=a[i]<6):
		i3=i3+1
		m=m+a[i]
	if(a[i]==max(a)):
		n=s[i]
	i=i+1
quantidade=i2+i3
me=m/quantidade
print(i1)
print(i2)
print(i3)
print(round(me,2))
print(n)

	



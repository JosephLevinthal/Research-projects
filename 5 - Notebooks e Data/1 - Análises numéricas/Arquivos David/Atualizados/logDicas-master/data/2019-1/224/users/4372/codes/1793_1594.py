from numpy import*
v=array(eval(input("vetor: ")))
i=0
a=0
x=0
c=1
while(i<size(v)):
	x=x+(v[a]*c)
	a=a+1
	c=c+1
	i=i+1
print(x)
from numpy import*
x= input("digite a cor de cabelo das pessoas:").split(',')
t=0
p=0
c=0
r=0
l=0
b=0
v=zeros(5,dtype=int)
for i in range(size(x)):
	if (x[i]=="P"):
		p=p+1
		v[0]=p
	if(x[i]=="C"):
		c=c+1
		v[1]=c
	if(x[i]=="R"):
		r=r+1
		v[2]=r
	if(x[i]=="L"):
		l=l+1
		v[3]=l
	if (x[i]=="B"):
		b=b+1
		v[4]=b
print(max(v))
print(v)



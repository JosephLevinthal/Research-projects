from numpy import*

a=array(eval(input('numero de gols do time: ')))
b=array(eval(input('numero de gols feito pelo time adversario: ')))
c=zeros(3, dtype=int)
for i in range(size(a)):
	if(a[i]>b[i]):
		c[0]=c[0]+1
	elif(a[i]==b[i]):
		c[1]=c[1]+1
	else:
		c[2]=c[2]+1
print(c)
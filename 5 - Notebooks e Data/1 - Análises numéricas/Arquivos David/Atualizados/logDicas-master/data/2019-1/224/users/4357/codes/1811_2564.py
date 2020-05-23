from numpy import*
time1=array(eval(input("digite o numero:")))
time2=array(eval(input("digite o numero:")))
resultado= time1-time2
a=0
b=0
c=0
for i in resultado:
	if(i==0):
		c=c+1
	elif(i>0):
		a=a+1
	else:
		b=b+1
d=zeros(3,dtype=int)
d[0]=a
d[1]=c
d[2]=b
print(d)


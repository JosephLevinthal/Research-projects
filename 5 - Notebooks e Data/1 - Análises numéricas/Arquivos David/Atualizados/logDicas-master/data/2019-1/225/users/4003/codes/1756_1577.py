from numpy import*

a=array(eval(input("a aceleracao:")))
v=array(eval(input("v0:")))
n=array(eval(input("numeros int.:")))
t=arange(n)
d=zeros(n)
i=0

while(i<n):
	d[i]=((a*(t[i]**2)/2)+v*t[i])
	i=i+1
print(d)
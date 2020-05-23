from numpy import*
x=array(eval(input()))
a=0
b=0
for i in range(size(x)):
	if(x[i]%2==1):
		b+=1

y=zeros(b,dtype=int)

u=0

for k in range(size(x)):
	if(x[k]%2!=0):
		y[u]=x[k]
		u+=1
print(y)
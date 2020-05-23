from numpy import*

x=array(eval(input("")))

o=0

for i in range(size(x)):
	if (x[i]%5==0):
		o+=1
print(o)
a=zeros(o,dtype=int)

h=0


for i in range(size(x)):
	if (x[i]%5==0):
		a[h]=i
		h+=1
		

print(a)
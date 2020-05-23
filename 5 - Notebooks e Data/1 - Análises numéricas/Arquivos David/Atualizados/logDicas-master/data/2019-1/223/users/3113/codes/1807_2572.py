from numpy import*
a=array(eval(input("")))
f=0
d=0
for i in range(size(a)):
	if(a[i]% 2 == 0):
		f=f+0
	else:
		f=f+1
b=zeros(f,dtype=int)
for i in range(size(a)):
	if(a[i]% 2 != 0):
		b[d]=a[i]
		d=d+1
print(b)
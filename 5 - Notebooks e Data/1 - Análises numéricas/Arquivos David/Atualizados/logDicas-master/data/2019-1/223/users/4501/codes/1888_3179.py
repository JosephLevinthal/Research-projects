from numpy import*
a=array(eval(input("vetor: ")))
b=zeros(a, dtype=int)
c=0
for i in a:
	if(i!=1):
		c=c+1
d=zeros(c-1, dtype=int)
e=0
for i in a:
	if(a[i]!=1):
		d[e]=a[i]
		e=e+1
	else:
		b[c]=
print(d)		
	
		
	

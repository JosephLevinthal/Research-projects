from numpy import*
a=array(eval(input(": ")))
b=zeros(3, dtype=int)
for i in range(size(a)):
	if(a[i].upper()=="TV"):
		b[0]=b[0]+1
	if(a[i].upper()=="NETFLIX"):
		b[1]=b[1]+1
	if(a[i].upper()=="YOUTUBE"):
		b[2]=b[2]+1
print(b)
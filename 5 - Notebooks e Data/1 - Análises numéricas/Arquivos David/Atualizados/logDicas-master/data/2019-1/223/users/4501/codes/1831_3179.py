from numpy import*
a=array(eval(input("vetor: ")))
b=zeros(size(a), dtype=int)
c=size(a)
for i in range(size(a)):
	b[i]=a[c-1]
	c=c-1
print(b)	
	
	
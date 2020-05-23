from numpy import*
x=array(eval(input("matriculas: ")))
b=0
l=0
for i in x:
	if(i%2==0):
		b=b+1
	else:
		l=l+1
m=zeros(l,dtype(int))
b=0
for i in x:
	if(i%2 != 0):
		m[b]=m[b]+1
		b=b+1
print (m)
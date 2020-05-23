from numpy import*
x=array(eval(input("Digite as matriculas: ")))
b=0
l=0
for i in x:
	if(i%2==0):
		b=b+1
	else:
		l=l+1
m=zeros(b,dtype(int))
l=0
for i in x:
	if(i%2==0):
		m[l]=m[l]+i
		l=l+1
print(m)		
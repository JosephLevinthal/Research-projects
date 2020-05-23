from numpy import*

a=array(eval(input()), dtype=str)
b=zeros(3, dtype=int)
n=0
t=0
y=0
for i in range(size(a)):
	if (a[i].upper()=="NETFLIX"):
		n+=1
	elif (a[i].upper()=="TV"):
		t+=1
	elif (a[i].upper()=="YOUTUBE"):
		y+=1
b[0]=t
b[1]=n
b[2]=y
print(b)
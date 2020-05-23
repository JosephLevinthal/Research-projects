from numpy import*
a=array(eval(input("dia da semana: ")))
b=zeros(6, dtype=int)
for i in range(size(a)):
	if(a[i]==2):
		b[0]=b[0]+1
	if(a[i]==3):
		b[1]=b[1]+1
	if(a[i]==4):
		b[2]=b[2]+1
	if(a[i]==5):
		b[3]=b[3]+1
	if(a[i]==6):
		b[4]=b[4]+1
	if(a[i]==7):
		b[5]=b[5]+1
c=zeros(6)	
for i in range(size(b)):
	c[i]=round(((b[i]*100)/size(a)), 1)
print(c)	

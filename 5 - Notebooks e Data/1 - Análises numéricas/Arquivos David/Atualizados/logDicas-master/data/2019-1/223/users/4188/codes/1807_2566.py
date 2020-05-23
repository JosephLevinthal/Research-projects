from numpy import *
v=array(eval(input("faltas: ")))
a=zeros(6,dtype=int)
for i in range(size(v)) :
	if(v[i]==2):
		a[0]=a[0]+1
	if(v[i]==3):
		a[1]=a[1]+1
	if(v[i]==4):
		a[2]=a[2]+1
	if(v[i]==5):
		a[3]=a[3]+1
	if(v[i]==6):
		a[4]=a[4]+1
	if(v[i]==7):
		a[5]=a[5]+1
b=zeros(6)
for i in range(size(b)):
	b[i]=round((a[i]*100)/size(v),1)
print(b)
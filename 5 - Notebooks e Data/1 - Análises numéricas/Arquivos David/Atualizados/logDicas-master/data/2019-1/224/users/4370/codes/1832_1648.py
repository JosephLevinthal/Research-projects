from numpy import *
f= array(eval(input("vetor de frequencia:")))
rep=0
for i in f:
	if(i<70):
		rep=rep + 1
print(rep)
c=0
b=0
z=zeros(rep,dtype=int)
for i in f:
	if(i<70):
		z[b]=c
		b=b+1
	c=c+1
print(z)

	
	


		
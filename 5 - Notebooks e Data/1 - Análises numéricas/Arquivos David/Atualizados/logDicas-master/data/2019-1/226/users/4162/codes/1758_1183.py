from numpy import *
e=array(eval(input("insira os termos: ")))
i=0
neg=0
while(i<size(e)):
	if e[i]<0:
		neg=neg+1
	i=i+1
tf=size(e)-neg
vf=zeros(tf,dtype=int)
j=0
i=0

while (i<size(e)):
	if (e[i])>=0:
		vf[j]=e[i]
		j=j+1
	i=i+1
print(vf)
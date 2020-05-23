from numpy import*
f=array(eval(input("digite o vetor: ")))
s=zeros(6, dtype=int)
for i in range(size(f)):
	if(f[i]==2):
		s[0]=s[0]+1
	if(f[i]==3):
		s[1]=s[1]+1
	if(f[i]==4):
		s[2]=s[2]+1
	if(f[i]==5):
		s[3]=s[3]+1
	if(f[i]==6):
		s[4]=s[4]+1
	if(f[i]==7):
		s[5]=s[5]+1
cont=zeros(6, (dtype))
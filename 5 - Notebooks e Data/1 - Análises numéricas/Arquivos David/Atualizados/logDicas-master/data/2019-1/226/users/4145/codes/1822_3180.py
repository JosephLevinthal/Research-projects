from numpy import*
s= array(eval(input("vetor de sorotipos: ")))
x=zeros(4,dtype=int)
for i in range(size(s)):
	if(s[i]==1):
		x[0]=x[0]+1
	elif(s[i]==2):
		x[1]=x[1]+1
	elif(s[i]==3):
		x[2]=x[2]+1
	elif(s[i]==4):
		x[3]=x[3]+1
		
print(x)		
from numpy import*
x=zeros(6,dtype=float)
f = array(eval(input("vetor de faltas: ")))
for i in range(size(f)):
	if(f[i]==2):
		x[0]=x[0]+1
	elif(f[i]==3):
		x[1]=x[1]+1
	elif(f[i]==4):
		x[2]=x[2]+1
	elif(f[i]==5):
		x[3]=x[3]+1
	elif(f[i]==6):
		x[4]=x[4]+1
	elif(f[i]==7):
		x[5]=x[5]+1

for k in range(size(x)):
	x[k]=round(x[k]/size(f)*100,1)
#x=x.split('.')
print(x)		
		
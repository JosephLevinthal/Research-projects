from numpy import*
v=array(eval(input("insira: ")))
x=zeros(4, dtype=int)
for i in range (size(v)):
	if(v[i]==1):
		x[0]=x[0]+1
	elif(v[i]==2):
		x[1]=x[1]+1
	elif(v[i]==3):
		x[2]=x[2]+1
	elif(v[i]==4):
		x[3]=x[3]+1
print(x)


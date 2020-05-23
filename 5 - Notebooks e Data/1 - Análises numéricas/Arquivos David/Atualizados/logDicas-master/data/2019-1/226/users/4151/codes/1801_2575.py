from numpy import*
v=input("digite ").upper().split(",")
x=zeros(3, dtype=int)
for i in range(size(v)):
	if(v[i]=="TV"):
		x[0]=x[0]+1
	elif(v[i]=="NETFLIX"):
		x[1]=x[1]+1
	elif(v[i]=="YOUTUBE"):
		x[2]=x[2]+1
print(x)
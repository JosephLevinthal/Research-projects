from numpy import*
ti=array(eval(input("num.de gols: ")))
ad=array(eval(input("num. de gols do adversario: ")))
x=zeros(3,dtype=int)
for i in range(size(ti)):
	if(ti[i]>ad[i]):
		x[0]=x[0]+1
	elif(ti[i]==ad[i]):
		x[1]=x[1]+1
	elif(ti[i]<ad[i]):
		x[2]=x[2]+1
print(x)
from numpy import*
f=array(eval(input("digite as faltas: ")))
x=zeros(6)
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
	
for i in range(size(x)):
	x[i]=round((x[i]/size(f))*100,1)
print(x)
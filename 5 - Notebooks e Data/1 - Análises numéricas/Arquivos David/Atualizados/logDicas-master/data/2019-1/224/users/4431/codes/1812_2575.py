from numpy import*
x=array(eval(input("Digite as plataformas: ")))
j=0
y=0
u=0
for i in x:
	if(i.upper()=="TV"):
		j=j+1
	elif(i.upper()=="NETFLIX"):
		y=y+1
	elif(i.upper()=="YOUTUBE"):
		u=u+1
m=zeros(3,dtype(int))
m[0]=m[0]+j
m[1]=m[1]+y
m[2]=m[2]+u
print(m)
from numpy import*
m= array(eval(input("x: ")))
p= array(eval(input("x: ")))
c= array(eval(input("x: ")))
x=zeros(3, dtype=int)
for i in range(size(m)):
	if(m[i]>=5 and p[i]>=(0.75*c)):
		x[0]=x[0]+1
	elif(m[i]<5):
		x[1]=x[1]+1
	elif(p[i]<(0.75*c)):
		x[2]=x[2]+1
print(x)
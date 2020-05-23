from numpy import*

a=array(eval(input()))
b=array(eval(input()))
al=3
c=10.3
d=6.7
e=9.7
h=5
i=0
z=0
y=0
l=0
g=0
w=0
while(i<size(a)):
	if(a[i]=="ALONGAMENTO"):
		z= al*b[i]
	elif(a[i]=="CORRIDA"):
		y=c*b[i]
	elif(a[i]=="DANCA"):
		l=d*b[i]
	elif(a[i]=="ESCALADA"):
		g=e*b[i]
	elif(a[i]=="HIDROGINASTICA"):
		w=h*b[i]
	i+=1
print(z+y+l+g+w)
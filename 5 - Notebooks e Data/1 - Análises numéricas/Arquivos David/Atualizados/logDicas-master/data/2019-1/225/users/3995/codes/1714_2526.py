n=int(input("numero1:"))
m=int(input("numero2:"))
c=0 # valor n
x=1 # ele 
h=0 #valor n
d=0 #valor m
j=0 #valor m
while(x<n and x<m):
	if(n%x==0):
		c+=1
		h+=x
	elif(m%x==0):
		j+=1
		d+=x
	x+=1

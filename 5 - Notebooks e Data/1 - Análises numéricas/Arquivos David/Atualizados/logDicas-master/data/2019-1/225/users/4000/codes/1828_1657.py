from numpy import*
n = input("maior quantidade: ").split(',')
a=0
b=0
c=0
d=0
e=0

for i in range(size(n)):
	if(n[i] == "AZ"):
		a=a+1
	elif(n[i]=="CA"):
		b=b+1
	elif(n[i]=="FL"):
		c=c+1
	elif(n[i]=="PA"):
		d=d+1
	elif(n[i]=="WI"):
		e=e+1
v = zeros(5,dtype=int)
v[0]=a
v[1]=b
v[2]=c
v[3]=d
v[4]=e
j=max(v)
print(j)
print(v)

	
	
	

	
		

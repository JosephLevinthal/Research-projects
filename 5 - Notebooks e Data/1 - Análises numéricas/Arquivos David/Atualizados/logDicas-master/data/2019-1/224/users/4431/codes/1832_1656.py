from numpy import*
x=input("Digite as silgas dos paises: ")
x=x.split(',')
b=0
e=0
f=0
j=0
p=0
for i in x:
	if(i=="BE"):
		b=b+1
	elif(i=="ES"):
		e=e+1
	elif(i=="FR"):
		f=f+1
	elif(i=="IT"):
		j=j+1
	elif(i=="PT"):
		p=p+1
m=zeros(5,dtype=int)
m[0]=m[0]+b
m[1]=m[1]+e
m[2]=m[2]+f
m[3]=m[3]+j
m[4]=m[4]+p
print(max(m))
print(m)

		
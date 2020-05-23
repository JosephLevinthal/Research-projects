from numpy import*
x=array(eval(input("Digite Numeros: ")))
y=0
f=0
m=0
while(y<(size(x))):
	if(x[f]>0):
		m=m+1
		f=f+1
		y=y+1
	else:
		f=f+1
		y=y+1
m=zeros(m,dtype=int)
j=0
b=0
v=0
while(j<(size(x))):
	if(x[b]>0):
		m[v]=m[v]+x[b]
		b=b+1
		v=v+1
		j=j+1
	else:
		b=b+1
		j=j+1
print(m)

	 	  		
		



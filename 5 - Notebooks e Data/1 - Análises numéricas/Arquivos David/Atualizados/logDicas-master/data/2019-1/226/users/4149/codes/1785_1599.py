from numpy import*

com=array(eval(input("entre com a lista de compras")))
a=size(com)
i=0
z=zeros(a, dtype=float)

while(i<size(com)):
	if(com[i]> 80):
		c= com[i]-((15*com[i])/100)
		z[i]=c
	i=i+1
j=0
c=zeros(a,dtype=float)
while(j<size(com)):
	if(com[j]<80):
		c[j]=com[j]
	j=j+1
vetr=z+c
	
print(round(sum(vetr),2))
	
	
		
		
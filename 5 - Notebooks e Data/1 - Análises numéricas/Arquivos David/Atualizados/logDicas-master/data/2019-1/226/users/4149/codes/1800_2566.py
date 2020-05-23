from numpy import*

f=array(eval(input("Entre com o vetor:")))

v=zeros(6)

for i in range(size(f)):
	if f[i]==2:
		v[0]=v[0]+1
	elif f[i]==3:
		v[1]=v[1]+1
	elif f[i]==4:
		v[2]=v[2]+1
	elif f[i]==5:
		v[3]=v[3]+1
	elif f[i]==6:
		v[4]=v[4]+1
	elif f[i]==7:
		v[5]=v[5]+1

for i in range(size(v)):
	v[i]=round(v[i]/size(f)*100,1)
	
print(v)
		
	


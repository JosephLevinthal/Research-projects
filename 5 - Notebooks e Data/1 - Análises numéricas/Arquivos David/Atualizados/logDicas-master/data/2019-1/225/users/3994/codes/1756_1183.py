from numpy import*
n = array(eval(input("Digite o vetor: ")))
i=0
j=0 
while(i<size(n)):
	if(n[i]>0):
		j=j+1
	i=i+1
i=0
v=zeros(j, dtype = int)
j=0
while(j<size(v)):
	if(n[i]>=0):
		v[j]=n[i]
	else:
		while(n[i]<0):
			i=i+1
		v[j]=n[i]
	i=i+1
	j=j+1
print(v)


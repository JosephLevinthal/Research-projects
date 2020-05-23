from numpy import*

n=array(eval(input("q?")))

for j in range(4):
	v=zeros(4)
	k=0
	for i in range(4):
		v[k]=n[i,j]
		k+=1
	v=sorted(v,reverse=True)
	k=0
	for i in range(4):
		n[i,j]=v[k]
		k+=1
print(n)
from numpy import*
n=array(eval(input("digite um vetor: ")))
d=zeros(size(n), dtype=int)

for i in range(size(n)):
	d[i]=n[i]
for i in range (size(n)):
	if(n[i]==1):
		for j in range(i,size(n)-1):
			d[j]=n[j+1]
			print(j)
		d[-1]=1
			
print(d)
		
		
		
		

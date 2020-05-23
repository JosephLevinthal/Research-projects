from numpy import*
a=0
c=0
v= array(eval(input("Insira o vetor:")))	

for i in range(size(v)):
	if(v[i] % 2 != 0):
		a+=1	
		cont= zeros(a,dtype=int)
for i in range(size(v)):
	if(v[i] % 2 != 0):
		cont[c]=v[i]
		c+=1
print(cont)
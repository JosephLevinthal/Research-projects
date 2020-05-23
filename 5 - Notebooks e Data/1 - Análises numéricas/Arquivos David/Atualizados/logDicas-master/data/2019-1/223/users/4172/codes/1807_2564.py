from numpy import*

vet =array(eval(input("")))
vet1 =array(eval(input("")))

a = zeros(3,dtype=int)


for i in range(size(vet)): 
	if (vet[i]>vet1[i]):
		a[0]+=1
	if (vet[i]==vet1[i]):
		a[1]+=1
	if(vet[i]<vet1[i]):
		a[2]+=1	
print(a)
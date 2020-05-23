from numpy import*
n=input("digite o numero:")
copy=""
i=0
while(i<len(n)):
	if((i+1)%3==0 and i<(len(n)-1)):
		copy=copy+str(n[i])+"."
	else:
		copy=copy+str(n[i])
	i=i+1
print(copy)
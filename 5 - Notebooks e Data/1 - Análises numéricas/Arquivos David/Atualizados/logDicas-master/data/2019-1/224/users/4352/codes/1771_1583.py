from numpy import*
n = input("digite algarismos: ")
i=0
b=""
while(i<len(n)):
	if((i+1)%3==0) and (i<(len(n)-1)):
		b=b+str(n[i])+"."
	else:
		b=b+str(n[i])
	i=i+1
print(b)	

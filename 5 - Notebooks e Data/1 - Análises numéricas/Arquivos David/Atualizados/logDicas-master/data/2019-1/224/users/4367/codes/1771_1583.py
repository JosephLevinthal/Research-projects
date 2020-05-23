from numpy import*
a=input("digite os valores: ")
b=""
i=0
while(i<len(a)):
	if((i+1)%3==0) and (i<(len(a)-1)):
		b=b+str(a[i])+"."
	else:
		b=b+str(a[i])
	i=i+1
print(b)
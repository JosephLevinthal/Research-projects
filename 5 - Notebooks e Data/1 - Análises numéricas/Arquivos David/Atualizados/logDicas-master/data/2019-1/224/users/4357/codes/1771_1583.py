from numpy import*
numero=input("digite o numero:")
c=""
i=0
while(i<len(numero)):
	if((i+1)%3==0 and i<(len(numero)-1)):
		c=c+str(numero[i])+"."
	else:
		c=c+str(numero[i])
	i=i+1
print(c)
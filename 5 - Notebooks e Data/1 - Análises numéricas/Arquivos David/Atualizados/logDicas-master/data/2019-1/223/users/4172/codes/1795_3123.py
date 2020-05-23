from numpy import*

x=array(eval(input("")))
i=0
co=0
m=x[0]**(-1)
while(i<size(x)):
	m+=m+x[i]**(-1)
	a=m/size(x)
	i+=1
	co+=1
print(round(a,2))
from numpy import *
comprasI = array(eval(input()))
desc = 0.15
i = 0
total = 0
aux = 0
while(i<size(comprasI)):
	if(comprasI[i]>80):
		aux = comprasI[i] 
		aux = aux - (aux * desc)
		comprasI[i]=aux
	total=total + comprasI[i]
	i=i+1
print(round(total,2))
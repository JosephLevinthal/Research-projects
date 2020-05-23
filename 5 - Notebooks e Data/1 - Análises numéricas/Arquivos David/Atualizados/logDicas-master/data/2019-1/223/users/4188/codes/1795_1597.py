from numpy import *
a=array(eval(input("custo: ")))
n=0
while(n < size(a)):
	if(a[n] < 80):
		a=sum(a)
	else:
		a = sum(a) - 5
	n= n+1
print(round(a,2))
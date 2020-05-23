from numpy import *
n=array(eval(input("numeros: ")))
p=0
m=1
while(p<size(n)):
	if(n[p]>=0):
		m=m*(n[p])
		M=m**(1/size(n))
		p=p+1
print(float(round(M,2)))
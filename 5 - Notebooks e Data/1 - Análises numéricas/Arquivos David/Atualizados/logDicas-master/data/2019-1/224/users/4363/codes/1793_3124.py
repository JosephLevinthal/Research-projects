from numpy import *
v=array(eval(input("digite n numeros:")))
n=size(v)
i=0
m=1
while(i<size(v)):
	m=m*(v[i])
	i=i+1
	M=m**(1/n)
print(round(M,2))		
      
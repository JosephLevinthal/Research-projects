from numpy import *
n=int(input())
a="*"
b="o"
i=2
j=n-1
print(a*2*n)
	
while(i<(2*n)):
	
	print(j*a + i*b +j*a)
	i=i+2
	j=j-1

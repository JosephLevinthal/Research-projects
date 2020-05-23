from numpy import*
a=array(eval(input("digite o vetor: ")))
n=size(a)
m=0
i=0
while(i<n):
	m=m+((a[i])**-1)
	i=i+1
M=(m/n)**-1
print(round(M, 2))
	
from numpy import*
a=array(eval(input("digite o vetor: ")))
i=0
s=0
v=0
b=0
while(i<size(a)):
	b=b+1
	s=s+(a[i])*b
	i=i+1
print(s)
	
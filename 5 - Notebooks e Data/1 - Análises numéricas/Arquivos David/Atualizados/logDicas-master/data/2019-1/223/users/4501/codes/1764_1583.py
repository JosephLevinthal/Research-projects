from numpy import*
a=input("string: ")
b=""
i=0
while(i<len(a)):
	i0=i
	i1=i+3
	b=b+a[i0:i1]+"."
	i=i+3
print(b[:-1])


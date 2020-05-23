from numpy import*

a=array(eval(input("")))
b= array(eval(input("")))
n=arange(size(a))

i=0
while(i < size(n)):
	n[i]=a[i]-b[i]
	i += 1

i = 0
while(i < size(n)):
	if (n[i] == max(n)):
		print(i+1)
	i += 1



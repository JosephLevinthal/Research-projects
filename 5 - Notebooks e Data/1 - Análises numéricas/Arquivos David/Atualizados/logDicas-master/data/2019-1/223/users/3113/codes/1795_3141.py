from numpy import*

n=array(eval(input("")))

i=0
d=0
w=1/6
while(i<size(n)):
	s=(n[i]**w)
	d=d+s
	i=i+1
m=(d/size(n))**6
print(round(m,2))
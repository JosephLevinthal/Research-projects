from numpy import*
n=array(eval(input("nivel:")))

a=0
i=0

while(i<size(n)):
	if(n[i]>99):
		a=a+1
		print(i)
	else:
		a=a+0
	i=i+1
print(a)
from numpy import*
a=array(eval(input("glicose: ")))
i=0
x=0
while(i<size(a)):
	if(a[i]>99):
		x=x+1
		print(i)
	else:
		x=x+0
	i=i+1
print(x)
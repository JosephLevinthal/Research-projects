from numpy import*
glicose=array(eval(input("digite o numero:")))
a=0
i=0
while(i<size(glicose)):
	if(glicose[i]>99):
		print(i)
		a=a+1
	else:
		a=a+0
	i=i+1
print(a)

from numpy import*

x=array(eval(input("")))

i=0
co1=0

while(i<size(x)):
	if(x[i]>99):
		co1+=1
		print(i)
	i+=1
print(co1)
		
		
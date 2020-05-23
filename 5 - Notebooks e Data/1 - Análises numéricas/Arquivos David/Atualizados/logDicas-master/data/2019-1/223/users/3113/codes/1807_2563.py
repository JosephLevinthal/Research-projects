from numpy import*
a=array(eval(input("")))
while(size(a)>1):
	d=0
	for i in a:
		if(i>=5 and i<7):
			d=d+1
	print(d)
	a=array(eval(input("")))
	
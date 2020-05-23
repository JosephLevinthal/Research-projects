from numpy import*
x = array(eval(input("x:")))

while(size(x)>1):
	aprov=0
	for e in x:
		if(e>=5 and e<7):
			aprov=aprov+1
	print(aprov)
	x = array(eval(input("x:")))
	
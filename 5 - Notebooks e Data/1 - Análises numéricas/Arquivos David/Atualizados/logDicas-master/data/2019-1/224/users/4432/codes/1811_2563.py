from numpy import*
y=array(eval(input("medias finais")))
x=0
while(size(y)>1):
	x=0
	for a in y:
		if(a>=5) and (a<7):
			x=x+1
	print(x)
	y=array(eval(input(" meida   ")))
from numpy import *
a = array(eval(input("media: ")))
while(size(a)>1):
	b = 0
	for i in range(size(a)):
		if(a[i]>=5 and a[i]<7):
			b = b + 1
	print(b)
	a = array(eval(input("media: ")))
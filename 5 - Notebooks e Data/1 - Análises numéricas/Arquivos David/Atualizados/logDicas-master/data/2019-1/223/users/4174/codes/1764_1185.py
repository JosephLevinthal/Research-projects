from numpy import*
a = array(eval(input("glicose:")))
b = 0
c = 0
while(b < size(a)):
	if(a[b] > 99 ):
		print(b)
		c = c + 1
	b = b + 1
print(c)
from numpy import*

a = array(eval(input()), dtype = int)
b = array(eval(input()), dtype = int)
c = array([], dtype = int) #the inverted b

i = size(b) - 1
while(i >= 0):
	c = append(c, [b[i]])
	i = i - 1

i = 0
while(i < size(a)):
	if(a[i] >= c[i]):
		print(a[i])
	else:
		print(c[i])
	
	i = i + 1
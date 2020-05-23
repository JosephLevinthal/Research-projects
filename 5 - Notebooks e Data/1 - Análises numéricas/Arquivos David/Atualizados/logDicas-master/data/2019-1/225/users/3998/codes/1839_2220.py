from numpy import*

m = array(eval(input()))

for i in range(shape(m)[0]):
	print(max(m[i,:]))
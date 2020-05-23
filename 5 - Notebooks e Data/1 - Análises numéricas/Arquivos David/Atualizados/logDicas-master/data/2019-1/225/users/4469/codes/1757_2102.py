from numpy import*

v = array(eval(input()))

i = 0
while(i < size(v)):
	if(v[i] % 2 != 0):
		v[i] = 0
	
	i = i + 1

print(v)
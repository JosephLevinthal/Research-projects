from numpy import*

v = array(eval(input()))

i = 0
s = 0

while(i < size(v)):
	if(v[i] > 99):
		print(i)
		s = s + 1
	
	i = i + 1

print(s)

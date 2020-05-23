from numpy import*

d = array(eval(input("")))

i = 0 
s = 0 
e = 1
while(i < size(d)):
	s = s + d[i]*e
	i = i+1
	e = e+1
	
print(s)
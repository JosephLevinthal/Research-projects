from numpy import *
v = array(eval(input("")))
for i in range(len(v)):
	if v[i]%2!=0:
		v[i]=0
print(v)
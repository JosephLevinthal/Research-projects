from numpy import *
v = array(eval(input("")))
i = 0
acu = 0
while(i<len(v)):
	if(v[i]>99):
		print(i)
		acu+=1
	i+=1
print(acu)
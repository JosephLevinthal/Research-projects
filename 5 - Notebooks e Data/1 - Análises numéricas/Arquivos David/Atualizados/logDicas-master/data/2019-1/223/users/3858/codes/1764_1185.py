from numpy import *
x = array(eval(input()))
i = 0
total = 0
while(i<size(x)):
	if(x[i]>99):
		print(i)
		total = total+1
	i = i +1
print(total)
	
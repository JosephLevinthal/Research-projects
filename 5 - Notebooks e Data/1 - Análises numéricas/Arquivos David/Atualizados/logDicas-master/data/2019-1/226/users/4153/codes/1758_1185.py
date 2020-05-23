from numpy import *

v = array(eval(input("Indhavs: ")))
i = 0
x = 0
while(i < size(v)):
	if(v[i] > 99):
		print(i)
		x = x + 1
	i = i + 1
print(x)
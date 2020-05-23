from numpy import *
gc = array(eval(input("v: ")))
i = 0
n = 0
while(i < size(gc)):
	if(gc[i]>99):
		print(i)
		n = n + 1
	i = i + 1
print(n)
from numpy import *

ve = input("")

x = ""

for i in range(len(ve)):
	print(ve[i])
	if ve[i] == "a" or ve[i] == "A":
		a = 0
	else:
		x += ve[i]
	
print(x)

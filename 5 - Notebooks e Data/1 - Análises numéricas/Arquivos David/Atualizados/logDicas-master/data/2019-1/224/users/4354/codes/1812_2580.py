from numpy import *
string = input('digite a string: ')
copy = ""
b = 1
for i in string:
	v = string[b]
	if(i == v):
		copy = copy + str(b)	
	b = b + 1
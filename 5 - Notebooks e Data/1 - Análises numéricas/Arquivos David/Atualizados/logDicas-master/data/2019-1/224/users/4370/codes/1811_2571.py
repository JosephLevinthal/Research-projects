from numpy import *
string = input("digite a string: ")
copy = ""
for i in string:
	if(i != "a" and i != "A"):
		copy = copy + i
print(copy)
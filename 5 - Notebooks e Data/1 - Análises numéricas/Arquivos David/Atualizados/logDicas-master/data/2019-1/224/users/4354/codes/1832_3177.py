from numpy import *
string = input("digite a string: ")
a,e,i,o,u = 0,0,0,0,0
for j in string:
	if(j == "a"):
		a = a + 1
	if(j == "e"):
		e = e + 1
	if(j == "i"):
		i = i + 1
	if(j == "o"):
		o = o + 1
	if(j == "u"):
		u = u + 1
print("a:",a)
print("e:",e)
print("i:",i)
print("o:",o)
print("u:",u)
		
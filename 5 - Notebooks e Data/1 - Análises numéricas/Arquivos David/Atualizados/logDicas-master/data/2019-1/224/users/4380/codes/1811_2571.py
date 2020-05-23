from numpy import *
a=input("numeros: ")
for x in a:
	a=a.replace("a","")
	a=a.replace("A","")
print(a)
from numpy import*
a = input("v: ")
for x in a:
	a = a.replace("a","")
	a = a.replace("A","")
print(a)
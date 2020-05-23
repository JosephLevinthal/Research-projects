from numpy import*
a = input("aqui: ")
for x in a:
	a = a.replace("a","")
	a = a.replace("A","")
print(a)
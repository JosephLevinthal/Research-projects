from numpy import*
a = input("Fala parceria :")
for x in a:
	a = a.replace("a","")
	a = a.replace("A","")
print(a)
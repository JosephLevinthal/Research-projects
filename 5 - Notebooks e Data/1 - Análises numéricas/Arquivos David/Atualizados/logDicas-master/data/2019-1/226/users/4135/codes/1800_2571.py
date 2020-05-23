from numpy import*
a=input("digite uma string: ")
for x in a:
	a=a.replace("a","")
	a=a.replace("A","")
print(a)	
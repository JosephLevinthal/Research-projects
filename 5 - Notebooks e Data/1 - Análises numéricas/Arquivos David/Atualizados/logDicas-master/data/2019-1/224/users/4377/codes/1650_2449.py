a=float(input("a"))
b=float(input("b"))
c=float(input("c"))
d=float(input("d"))
e=float(input("e"))
f=float(input("f"))

h=(a*e - b*d)

x = (c*e - b*f) // h
y = (a*f - c*d) // h

if (h != 0):  
	print(x)
	print(y)
   
else:
	print("Nao tem solucao")



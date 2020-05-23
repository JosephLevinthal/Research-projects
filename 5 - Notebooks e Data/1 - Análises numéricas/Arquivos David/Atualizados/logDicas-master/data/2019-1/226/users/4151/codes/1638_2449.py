a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
d=float(input("d: "))
e=float(input("e: "))
f=float(input("f: "))


if(a*e - b*d != 0):
	print((c*e - b*f)/(a*e - b*d))
	print((a*f -c*d)/(a*e - b*d))
else:
	print("Nao tem solucao")
	

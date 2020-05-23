a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))

q = a*e - b*d




if (q == 0):
	print("Nao tem solucao")
	
else:
	x = (c*e - b*f)/q
	y = (a*f - c*d)/q
	print(x,y)
	


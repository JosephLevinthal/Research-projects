a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))
x1 = ((c * e) - (b * f)) 
z1 = ((a * e) - (b * d))
y1 = ((a * f) - (c * d))
if (z1 != 0):
	print( x1/z1)
	print( y1/z1)
else:
	print("Nao tem solucao")
	
	
		
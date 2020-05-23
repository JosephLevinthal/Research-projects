a = float(input("A: "))
b = float(input(""))
c = float(input(""))
d = float(input(""))
e = float(input(""))
f = float(input(""))
x = a*e-b*d
if(x<0):
	z = (c * e - b * f)/x
	y = (a*f-c*d)/x
	print(z)
	print(y)
else:
	print("Nao tem solucao")
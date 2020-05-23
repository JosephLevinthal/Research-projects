a = float(input("valor de a:"))
b = float(input("valor de b:"))
c = float(input("valor de c:"))
d = float(input("valor de d:"))
e = float(input("valor de e:"))
f = float(input("valor de f:"))
z = (a*e)-(b*d)
x = (c*e)-(b*f)

y = (a*f)-(c*d)

if (z == 0):
	print("Nao tem solucao")

else:
	aa = x/z
	bb = y/z
	
	print(aa)
	print(bb)
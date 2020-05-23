a = float(input("Coeficiente a:"))
b = float(input("Coeficiente b:"))
c = float(input("Coeficiente c:"))
d = float(input("Coeficiente d:"))
e = float(input("Coeficiente e:"))
f = float(input("Coeficiente f:"))
x = (c*e)-(b*f)
x1 = (a*e)-(b*d)
y = (a*f)-(c*d)


if (x1 == 0):
	print("Nao tem solucao")
else:
	print(x/x1)
	print(y/x1)
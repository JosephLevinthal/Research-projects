a = float(input("digite o coeficiente a:"))
b = float(input("digite o coeficiente b:"))
c = float(input("digite o coeficiente c:"))
d = float(input("digite o coeficiente d:"))
e = float(input("digite o coeficiente e:"))
f = float(input("digite o coeficiente f:"))
s = (a*e) - (b*d)
if (s == 0):
	print("Nao tem solucao")
else:
	print(((c*e) - (b*f)) / ((a*e) - (b*d)))
	print(((a*f) - (c*d)) / ((a*e) - (b*d)))
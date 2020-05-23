from math import*
a = float(input("Coeficiente a:"))
b = float(input("Coeficiente b:"))
c = float(input("Coeficiente c:"))
d = float(input("Coeficiente d:"))
e = float(input("Coeficiente e:"))
f = float(input("Coeficiente f:"))
if(a*e-b*d != 0):     #Condição 
	x = (c*e-b*f)/(a*e-b*d)
	y = (a*f-c*d)/(a*e-b*d) 
	print(x)
	print(y)
else:
	print("Nao tem solucao")

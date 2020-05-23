a = float(input("Coeficiente a:"))
b = float(input("Coeficiente b:"))
c = float(input("Coeficiente c:"))
d = float(input("Coeficiente d:"))
e = float(input("Coeficiente e:"))
f = float(input("Coeficiente f:"))

x = ((c*e) - (b*f))  
y = ((a*f) - (c*d)) 
x1 = ((a*e) - (b*d))
x2 = ((a*e) - (b*d))

if(x1 == 0):
	msg = "Nao tem solucao"
	print(msg)
else:
	msg = x/x1
	msg1 = y/x1
	print(msg)
	print(msg1)


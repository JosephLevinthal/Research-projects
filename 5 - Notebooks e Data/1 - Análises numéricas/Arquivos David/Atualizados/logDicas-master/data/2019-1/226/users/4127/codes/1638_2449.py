a= float(input("qual seu coeficiente a? "))
b= float(input("qual seu coeficiente b? "))
c= float(input("qual seu coeficiente c? "))
d= float(input("qual seu coeficiente d? "))
e= float(input("qual seu coeficiente e? "))
f= float(input("qual seu coeficiente f? "))
h= (a*e-b*d)

if (h != 0):
	print((c*e-b*f)/h, (a*f-c*d)/h)
else:
	print("Nao tem solucao")

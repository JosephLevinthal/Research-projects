a= float(input("insira o coeficiente a: "))
b= float(input("insira o coeficiente b: "))
c= float(input("insira o coeficiente c: "))
d= float(input("insira o coeficiente d: "))
e= float(input("insira o coeficiente e: "))
f= float(input("insira o coeficiente f: "))
de=(a*e-b*d)
if de==0:
	print("Nao tem solucao")
else:
	print((c*e-b*f)/de)
	print((a*f-c*d)/de)

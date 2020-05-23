#erro quando
a=int(input("coeficiente a: "))
b=int(input("coeficiente b: "))
c=int(input("coeficiente c: "))
d=int(input("coeficiente d: "))
e=int(input("coeficiente e: "))
f=int(input("coeficiente f: "))
if(a*e-b*d==0):
	print("Nao tem solucao")

else:
	print((c*e-b*f)/(a*e-b*d))
	print((a*f-c*d)/(a*e-b*d))

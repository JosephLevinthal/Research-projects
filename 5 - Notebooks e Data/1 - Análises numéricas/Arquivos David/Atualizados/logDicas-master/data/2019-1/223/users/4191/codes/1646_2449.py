a=float(input("Coeficiente: "))
b=float(input("Coeficiente: "))
c=float(input("Coeficiente: "))
d=float(input("Coeficiente: "))
e=float(input("Coeficiente: "))
f=float(input("Coeficiente: "))


if((a*e)-(b*d)==0):
	print("Nao tem solucao")
else:
	x=((c*e)-(b*f))/((a*e)-(b*d))
	y=((a*f)-(c*d))/((a*e)-(b*d))
	
	print(x)	
	print(y)
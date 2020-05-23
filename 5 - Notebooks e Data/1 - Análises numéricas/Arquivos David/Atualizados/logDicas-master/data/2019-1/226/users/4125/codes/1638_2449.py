a = float(input("digite um coeficiente: "))
b = float(input("digite um coeficiente: "))
c = float(input("digite um coeficiente: "))
d = float(input("digite um coeficiente: "))
e = float(input("digite um coeficiente: "))
f = float(input("digite um coeficiente: "))

if ((a*e) - (b*d) !=0):
	x = ((c*e)-(b*f))/((a*e)-(b*d))
	print(x)
if (((a*e)-(b*d))!=0):
	y=((a*f)-(c*d))/((a*e)-(b*d))
	print(y)
else:
	print("Nao tem solucao")

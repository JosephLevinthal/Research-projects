a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))
d = float(input("Digite o coeficiente d: "))
e = float(input("Digite o coeficiente e: "))
f = float(input("Digite o coeficiente f: "))
if((a*e)-(b*d)!=0):
	x = ((c*e)-(b*f))/((a*e)-(b*d))
	y = ((a*f)-(c*d))/((a*e)-(b*d))
	print(x)
	print(y)
else:
	print("Nao tem solucao")
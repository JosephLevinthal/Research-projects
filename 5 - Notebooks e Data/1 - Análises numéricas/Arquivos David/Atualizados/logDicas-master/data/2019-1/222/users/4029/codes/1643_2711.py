a= float(input("Valor disponivel: "))
b= int(input("Quantidades de tickets do RU: "))
c= float(input("Valor dos tickets: "))
d= int(input("Quantidade de passes de onibus: "))
e= float(input("Valor dos passes: "))
f= ((b * c) + (d * e))
if (a >= f):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
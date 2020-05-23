a= float(input(" valor disponivel: "))
b= float(input(" quant. de tickets: "))
c= float(input(" valor dos ticketes: "))
d= float(input(" quant. passe busao: "))
e= float(input("valor dos passes: " ))
total= b*c+d*e

if (a>= total):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
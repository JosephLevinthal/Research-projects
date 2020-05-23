v = float(input("Valor disponivel: "))
qt = int(input("Quantidade de tickets: "))
vt = float(input("Valor dos tickets: "))
qp = int(input("Quantidade de passes de onibus: "))
vp = float(input("Valor dos passes: "))

if (v >= (qt*vt + qp * vp)):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
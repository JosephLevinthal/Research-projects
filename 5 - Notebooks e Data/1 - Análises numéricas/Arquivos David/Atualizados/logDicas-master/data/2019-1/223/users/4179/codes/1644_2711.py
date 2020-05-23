vd=float(input("Valor disponivel: "))
qt=int(input("Quantidade de tickets: "))
vt=float(input("Valor dos tickets: "))
qtp=int(input("Quantidade dos passes: "))
vp=float(input("Valor dos passes: "))
if (vd > qt*vt + qtp*vp):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
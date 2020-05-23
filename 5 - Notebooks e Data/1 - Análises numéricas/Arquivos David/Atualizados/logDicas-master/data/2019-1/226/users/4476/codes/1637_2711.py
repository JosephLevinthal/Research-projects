valor = int(input("valor disponivel: "))
qt = int(input("tickets RU: "))
valortk = float(input("valor dos tickets: "))
qp = int(input("passes: "))
vp = float(input("valor dos passes: "))

a = qt*valortk
b = qp*vp
vt = a + b

if (valor >= vt):
	print("SUFICIENTE")
	
else:
	print("INSUFICIENTE")
vd = float(input("Valor disponivel: "))
qnt = int(input("Quantidade de Tickets: "))
vt = float(input("Valor dos tickets: "))
qntb = int(input("Quantidade de passes no onibus: "))
vp = float(input("Valor dos passes do onibus: "))

eq = (qnt * vt) + (qntb * vp)

if (vd >= eq):
	msg = "suficiente".upper()
	
else:
	msg = "insuficiente".upper()
	
print(msg)
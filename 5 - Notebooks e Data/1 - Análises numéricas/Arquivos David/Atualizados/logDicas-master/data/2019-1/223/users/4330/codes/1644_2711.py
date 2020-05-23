valor=float(input("valor disponivel: "))
qt=int(input("quantidades de tickets do RU: "))
vt=float(input("valor dos tickets: "))
qp=int(input("quantidade de passes de ônibus: "))
vp=float(input("valor dos passes: "))

total= (qt*vt) + (qp*vp)

if ( valor >= total):
	print ("suficiente".upper())
	
else:
	print ("insuficiente".upper())
	

valor = float(input("valor disonivel:"))
qt = int(input("quantidades de tickes do RU:"))
vt = float(input("valor dos tickets:"))
qp = int(input("quantidades de passes de onibus:"))
vp = float(input("valor dos passes"))

total = (qt*vt) + (qp*vp)
if (valor >= total):
	print("suficiente".upper())
else:
	print("insuficiente".upper())
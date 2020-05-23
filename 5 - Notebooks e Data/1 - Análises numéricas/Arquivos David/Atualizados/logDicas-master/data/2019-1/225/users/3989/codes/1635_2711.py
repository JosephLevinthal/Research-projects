valor = float(input(""))
qtickets = int(input(""))
valort = float(input(""))
qp = int(input(""))
vp = float(input(""))

vtotal = qtickets * valort + qp * vp 
if (valor>=vtotal):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
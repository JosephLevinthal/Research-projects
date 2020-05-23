v = float(input("valor:"))
q = int(input("quantidade: "))
vt = float(input("valorticket: "))
qp = int(input("quantidadepasse:"))
vp = float(input("valorpasse: "))

if ((q * vt) + (qp * vp)<= v):
	msg = "SUFICIENTE"
else:
	msg = "INSUFICIENTE"

print(msg)
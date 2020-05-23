v = float(input("valor disponivel:"))
ru = int(input("quantidade:"))
vt = float(input("valor dos tickets:"))
po = int(input("passes de onibus:"))
vp = float(input("valor dos passes:"))
if(v >= (ru*vt) + (po*vp)):
	msg = "SUFICIENTE"
else:
	msg = "INSUFICIENTE"
print(msg)
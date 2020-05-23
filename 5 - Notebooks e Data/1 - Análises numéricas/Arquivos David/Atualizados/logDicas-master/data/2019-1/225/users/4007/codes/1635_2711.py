vd = float(input("valor disponivel: "))
qtrc = int(input("quantidades de tickets:"))
vt = float(input("valor dos tickets: "))
qpo = int(input("quantidade de passes: "))
vp = float(input("valor dos passes: "))
total = (qtrc*vt) + (qpo*vp)

if (vd >= total):
	msg = "suficiente"
	
else: 
	msg = "insuficiente"
	
print(msg.upper())


vd=float(input("valor disponivel:"))
qtru=float(input("quantidade de tickets do ru:"))
vdt=float(input("valor dos tickets:"))
qpdo=float(input("quantidades de passes de onibus"))
vdp=float(input("valor dos passes"))
soma=(qtru*vdt)+(qpdo*vdp)
if(vd>=soma):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
v = float(input("valor disponivel:"))
ru = int(input("quantidade de tickets:"))
vru = float(input("valor do ticket:"))
qp = int(input("quantidade de passes:"))
vp = float(input("valor dos passes:"))
if(v >= ru*vru + qp*vp):
	print("suficiente".upper())
else:
	print("insuficiente".upper())
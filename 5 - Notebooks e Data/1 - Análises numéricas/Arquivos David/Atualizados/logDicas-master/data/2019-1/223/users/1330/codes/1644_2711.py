v = float(input())
qt = int(input())
vt = float(input())
qp = int(input())
vp = float(input())

if((vt*qt)+(vp*qp) <= v):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
valor=float(input("valor"))
qtt=int(input("a"))
vt=float(input("b"))
qtp=int(input("c"))
vp=float(input("d"))
if( (qtt*vt) + (qtp*vp) <= valor):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")